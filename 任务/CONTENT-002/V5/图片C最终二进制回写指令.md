# CONTENT-002｜图片C最终二进制回写指令｜V5

- project_id：XHS-BEAUTY-002
- task_id：CONTENT-002
- task_version：V5
- input_revision：4
- source_role：总监
- target_role：图片终审修图员C
- action：FINAL_BINARY_WRITEBACK_ONLY
- re_review_required：false
- regenerate_required：false
- rework_round_counted：false
- return_to_A_or_B：false
- audit_fixed_commit：8b0af7770914db1fc48153a5db061025dffc4a25
- audit_result：PASS
- P0：0
- P1：0
- P2：3
- score：93

## 只做一件事
把当前聊天已经由用户最终确认、并被独立审核PASS的4张实际最终图，原样写入GitHub新资产目录。

禁止重新生成、禁止修图、禁止改字、禁止改产品、禁止重新审核。

## 新资产目录
请写入：
资产/内容/CONTENT-002/LOCK-V2/

固定文件名：
1. 01_cover.jpg
2. 02_page.jpg
3. 03_page.jpg
4. 04_page.jpg

## 必须严格匹配的SHA-256
P1 / 01_cover.jpg
0b2ed7c4b100c9ffa6f7d30b442561090a1e6a20a2de4b9421ce78292113072a

P2 / 02_page.jpg
57c962ab451b24c92249f8ef653733b6ff63833702b641005baf1b0a35d8911a

P3 / 03_page.jpg
1570068fe9c907b8414779cc7090beae10c2cfe90f19c330317f0a48d2c26a67

P4 / 04_page.jpg
6f5a1039b08309c7c23b36552d5e918b01597eabbe3e9a2fff78f093611f6799

尺寸：1152×1536
实际编码：JPEG

任何一张SHA-256不一致，都不能声明完成。

## 历史保留
必须保留：
产物/图片C/CONTENT-002/V2-R1/交付.json

它属于历史REWORK_REQUIRED记录，不覆盖、不删除。

## 新C最终记录
请新建：
产物/图片C/CONTENT-002/V3/最终资产清单.json
产物/图片C/CONTENT-002/V3/交付.json

交付必须写：
- task_id=CONTENT-002
- task_version=V5
- input_revision=4
- result=PASS
- action=FINAL_BINARY_WRITEBACK_ONLY
- audit_fixed_commit=8b0af7770914db1fc48153a5db061025dffc4a25
- asset_root=资产/内容/CONTENT-002/LOCK-V2/
- 4张文件名、Git blob SHA、SHA-256、尺寸、格式
- user_accepted_current_images_as_final=true
- rework_required=false
- next_role=总监AI

## 已知一次性偏差
保留记录但不修改：
- CONTENT-002当前脚注为一次性接受
- P3底部产品版本问题为用户一次性接受
- 当前图片与文案V2非逐字复刻为已接受偏差

不要因此重新修改图片。

## 完成条件
4张二进制全部写入
→ 固定提交回读4/4
→ SHA-256 4/4一致
→ 新V3清单与交付回读
→ 返回最终固定提交给总监

完成后总监创建：
批准/CONTENT-002/LOCK-V2.json
并进入发布准备。
