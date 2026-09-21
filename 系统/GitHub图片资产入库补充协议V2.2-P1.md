# GitHub图片资产入库补充协议 V2.2-P1

## 1. 结论
GitHub可以直接保存JPG、JPEG、PNG等图片二进制。本项目从本协议生效起，把GitHub同时作为正式最终图片资产库。

## 2. 必须入库
### PERSONA最终资产
C PASS后的：
- master_face
- anchor_front
- anchor_45
- anchor_halfbody
- anchor_detail（若任务存在）

固定路径：
资产/人物/PERSONA-001/LOCK-Vn/

### CONTENT最终资产
每条CONTENT经C PASS后的全部最终发布图。

固定路径：
资产/内容/{task_id}/LOCK-Vn/

### 可选长期资产
用户自己提供并允许长期使用的产品参考图：
资产/产品参考/{asset_id}/

## 3. 默认不入库
A中间草稿、B返修中间图、被淘汰旧图、临时网页研究图。只保留其文字记录/来源即可。

## 4. 上传规则
必须是真实图片二进制。允许使用GitHub blob/tree/commit方式写入，二进制以base64传输。

禁止：
- 把base64字符串当文本写成.jpg
- 空占位文件
- 只有清单没有图片
- 声称上传但没有commit/blob

## 5. 每张图片必须记录
repo_path、commit、git_blob_sha、sha256、bytes、width、height、format。

## 6. 人物复用
后续图片A需要人物时：
1. 先读active_anchor_lock；
2. 从LOCK取得master_face和anchor的GitHub路径；
3. 当前工具能直接取得GitHub二进制作为视觉参考时自动使用；
4. 若当前图片编辑能力无法直接消费GitHub图片，再要求用户上传LOCK指定原图。
不得只靠文字重新随机生成“差不多的脸”。

## 7. 仓库体积
最终图建议长边1440至2048px，单张尽量不超过5MB。A/B中间废稿默认不上传。以后资产规模过大再拆独立assets仓库。

## 8. 公开仓库
当前仓库公开。项目原创虚拟人物和项目自有最终图可入库。真实个人照片上传前应确认用户愿意公开；含GPS等敏感元数据时应先去除敏感信息，不伪造新的拍摄来源。

## 9. 当前PERSONA兼容
当前PERSONA-001 input_revision=3不重跑A/B。
从C最终PASS开始执行：
C最终图 → GitHub二进制入库 → 总监核验 → PERSONA LOCK。
