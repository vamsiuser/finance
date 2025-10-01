from django.core.management.base import BaseCommand
import os
import stat
import zipfile
from io import BytesIO
from pathlib import Path
import paramiko


class Command(BaseCommand):
    help = 'Displays current time'
    
        
    def ensure_dir(self, path: Path):
        path.mkdir(parents=True, exist_ok=True)
        
    def sftp_connect(self, host, port, username, password=None, pkey_path=None) -> paramiko.SFTPClient:
        """
        Establish an SFTP connection and return an SFTPClient.
        """
        transport = paramiko.Transport((host, port))

        if pkey_path:
            key = None
            # Try RSA first; you can also add Ed25519 or ECDSA if needed
            try:
                key = paramiko.RSAKey.from_private_key_file(pkey_path)
            except paramiko.ssh_exception.PasswordRequiredException:
                raise RuntimeError("Your private key is encrypted; use ssh-agent or provide a decrypted key.")
            transport.connect(username=username, pkey=key)
        else:
            if password is None:
                raise RuntimeError("Must provide either PASSWORD or PRIVATE_KEY_PATH.")
            transport.connect(username=username, password=password)

        return paramiko.SFTPClient.from_transport(transport)
    def list_remote_zip_files(self, sftp: paramiko.SFTPClient, remote_dir: str):
        """
        Yield remote paths of regular files that end with .zip in the given directory (non-recursive).
        """
        for attr in sftp.listdir_attr(remote_dir):
            print(attr.filename)
            if self.is_regular_file(attr) and attr.filename.lower().endswith(".zip"):
                yield f"{remote_dir.rstrip('/')}/{attr.filename}"
    
    def is_regular_file(self, attr) -> bool:
        """Return True if the SFTPAttributes refer to a regular file."""
        return stat.S_ISREG(attr.st_mode)
    
    def download_and_extract_zip(self, sftp: paramiko.SFTPClient, remote_zip_path: str, local_extract_root: Path):
        """
        Download a remote .zip to memory and extract it to LOCAL_EXTRACT_ROOT/<zip_name_without_ext>/
        (No local .zip file is stored; extraction is done from memory.)
        """
        zip_name = Path(remote_zip_path).name
        dest_dir = local_extract_root / Path(zip_name).stem
        self.ensure_dir(dest_dir)

        # Read the entire remote zip into memory
        with sftp.open(remote_zip_path, "rb") as remote_f:
            zip_bytes = remote_f.read()

        with zipfile.ZipFile(BytesIO(zip_bytes)) as zf:
            zf.extractall(dest_dir)

        print(f"✔ Extracted: {remote_zip_path}  ->  {dest_dir}")

    def handle(self, *args, **kwargs):

        SFTP_HOST = "54.73.214.123"
        SFTP_PORT = 22
        SFTP_USERNAME = "sftpnewuser"
        SFTP_PASSWORD = "qwer1234"  # or set to None if using key auth

        # If using key auth, set PRIVATE_KEY_PATH and leave SFTP_PASSWORD=None
        PRIVATE_KEY_PATH = None  # e.g. "/home/you/.ssh/id_rsa" or None

        REMOTE_DIR = "uploads/"  # remote directory containing .zip files
        LOCAL_EXTRACT_ROOT = "unziped_files"  # local destination root
        # =====================================
        local_root = Path(LOCAL_EXTRACT_ROOT)
        self.ensure_dir(local_root)

        # Optional: host key handling (for production, verify host keys!)
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # NOTE: Accepts unknown hosts automatically

        # We’ll build an SFTP from Transport instead (keeps it simple for file ops)
        sftp = self.sftp_connect(
            SFTP_HOST,
            SFTP_PORT,
            SFTP_USERNAME,
            password=SFTP_PASSWORD,
            pkey_path=PRIVATE_KEY_PATH,
        )

        try:
            # 1) Download & extract ALL .zip files from REMOTE_DIR
            print(f"Scanning for .zip files in {REMOTE_DIR} ...")
            zips = list(self.list_remote_zip_files(sftp, REMOTE_DIR))
            print(zips,"111111111111111111111111111111111111111111111111111")
            if not zips:
                print("No .zip files found.")
            else:
                for remote_zip in zips:
                    self.download_and_extract_zip(sftp, remote_zip, local_root)
        finally:
            # Close the SFTP (and its underlying Transport)
            t = sftp.get_channel().get_transport() if hasattr(sftp, "get_channel") else None
            sftp.close()
            if t:
                t.close()