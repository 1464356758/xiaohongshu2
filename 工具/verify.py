#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XHS-BEAUTY-002 V2.2 static integrity verifier."""
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md","启动说明.md","数据库入口.json","当前进度.json","运营手册.md","角色工作流.md",
    "系统/共同协议.md","系统/状态机V2.2.md","系统/审核标准.md","系统/初始预算.json",
    "系统/图片工作流V2.md","系统/图片质量门禁.md","系统/图片资产交付协议V2.2.md",
    "系统/版本锁定协议.md","系统/热点与品牌借势协议V2.2.md",
    "系统/投放与预算闸门V2.2.md","系统/商务与财务口径V2.2.md",
    "数据/数据字典.md","任务/BOOT-001/V3/任务.json","任务/PERSONA-001/V2/任务.json",
]
ROLES = [
    "角色/01_总监.txt","角色/02_市场与定位研究员.txt","角色/03_热点与竞品研究员.txt",
    "角色/04_内容策划.txt","角色/05_文案脚本.txt","角色/06_图片生成员A.txt",
    "角色/07_图片审核修图员B.txt","角色/08_图片终审修图员C.txt",
    "角色/09_内容与合规审核.txt","角色/10_发布与社群运营.txt",
    "角色/11_数据分析与实验.txt","角色/12_增长投放.txt","角色/13_商务与财务.txt",
]
JSON_FILES = [
    "数据库入口.json","当前进度.json","系统/初始预算.json",
    "任务/BOOT-001/V3/任务.json","任务/PERSONA-001/V2/任务.json",
    "模板/任务.json","模板/交付.json","模板/内容任务.json",
    "模板/图片资产清单.json","模板/人物LOCK.json","模板/内容LOCK.json",
    "模板/数据快照.json",
]
LEGACY = [
    "角色/02_热点选题AI.txt","角色/03_文案脚本AI.txt","角色/04_图片生成员A.txt",
    "角色/05_图片审核修图员B.txt","角色/06_图片终审修图员C.txt",
    "角色/07_内容与合规审核AI.txt","角色/08_发布与社群运营AI.txt",
    "角色/09_数据分析AI.txt","系统/状态机V2.1.md","系统/图片资产交付协议V2.1.md",
]

errors=[]

for rel in REQUIRED + ROLES:
    if not (ROOT/rel).is_file():
        errors.append(f"MISSING: {rel}")

for rel in LEGACY:
    if (ROOT/rel).exists():
        errors.append(f"LEGACY_PRESENT: {rel}")

parsed={}
for rel in JSON_FILES:
    p=ROOT/rel
    if not p.is_file():
        errors.append(f"MISSING_JSON: {rel}")
        continue
    try:
        parsed[rel]=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"INVALID_JSON: {rel}: {e}")

db=parsed.get("数据库入口.json",{})
if db.get("project_id")!="XHS-BEAUTY-002":
    errors.append("BAD_PROJECT_ID")
if db.get("role_count")!=13:
    errors.append("BAD_ROLE_COUNT")
if db.get("state_machine_path")!="系统/状态机V2.2.md":
    errors.append("BAD_STATE_MACHINE_PATH")
if db.get("asset_protocol_path")!="系统/图片资产交付协议V2.2.md":
    errors.append("BAD_ASSET_PROTOCOL_PATH")

progress=parsed.get("当前进度.json",{})
task_path=progress.get("task_path")
if not task_path or not (ROOT/task_path).is_file():
    errors.append(f"BAD_CURRENT_TASK_PATH: {task_path}")

budget=parsed.get("系统/初始预算.json",{})
pools=budget.get("pools_cny",{})
if sum(pools.values()) != budget.get("capital_limit_cny"):
    errors.append("BUDGET_SUM_MISMATCH")

if len([p for p in ROLES if (ROOT/p).is_file()]) != 13:
    errors.append("ROLE_COUNT_ON_DISK_NOT_13")

if errors:
    print("FAIL")
    for e in errors:
        print(e)
    sys.exit(1)

print("PASS")
print("project_id=XHS-BEAUTY-002")
print("system_version=2.2")
print("role_count=13")
print(f"current_task={task_path}")
print(f"capital_limit_cny={budget.get('capital_limit_cny')}")
