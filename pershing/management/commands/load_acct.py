from django.core.management.base import BaseCommand, CommandError
from django.db import connection, transaction
from dataclasses import dataclass
from typing import Dict, List, Tuple
import itertools, datetime, os

from django.forms import ValidationError
from pershing.managers.command_managers.load_acct_files_manager import loadAcctFilesManager

@dataclass
class TableMeta:
    name: str
    columns: List[str]
    pk_cols: List[str]
    not_null: List[str]

class Command(BaseCommand):
    help = "Load ACCT/ACCF file into MySQL via Django"
    
    def __init__(self):
        self.loadactMng = loadAcctFilesManager()

    def add_arguments(self, parser):
        parser.add_argument("path", help="Path to ACCT/ACCF flat file")

    @transaction.atomic
    def handle(self, *args, **opts):
        path = opts["path"]
        if not os.path.exists(path):
            raise CommandError(f"File not found: {path}")
        try:
            line_len = 0
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                block = []
                for ln, raw in enumerate(fh, 1):
                    line_len +=1
                    line = raw.rstrip("\r\n")
                    block.append((ln, line))
                    if len(block) == 1:
                        self.loadactMng.process_block(block)
                        block = []
                if block:
                    self.loadactMng.process_block(block)
            print("successssssssssssssssssssssss", line_len)
        except ValidationError as e:
            raise CommandError(str(e),"vvvvvvvvvvvvvvvvvv")
        except Exception as e:
            raise CommandError(str(e),"eeeeeeeeeeeeeeeeeeeeeee")
        
