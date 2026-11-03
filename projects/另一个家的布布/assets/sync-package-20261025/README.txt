《另一个家的布布》资产同步包（Windows 11兼容版）

此包使用ASCII文件名，避免部分压缩软件/浏览器处理中文文件名时发生兼容问题。8张图片的原始字节未更改；manifest.json记录每张图片的大小与SHA-256。

内容：
- assets/：8张已确认的空间图片（文件名使用ASCII）
- sync_assets_to_github.ps1：Windows PowerShell同步脚本（UTF-8 BOM，兼容Windows PowerShell 5.1）
- manifest.json：图片校验清单
- docs/：剧本、空间关系说明、六张正视图核对表

Windows 11操作：
1. 右键ZIP，选择“全部解压缩…”，解压到一个单独文件夹。
2. 打开PowerShell（无需管理员权限）。
3. 运行：
   powershell -NoProfile -ExecutionPolicy Bypass -File "<解压目录>\sync_assets_to_github.ps1" -RepoPath "<本地agent-memory仓库路径>" -PackagePath "<解压目录>"
4. 检查脚本显示的8项SHA-256核验均为OK，以及Git暂存列表只包含8张图片后，再输入Y提交推送。
5. 上传完成后仍需校验GitHub远程文件的SHA-256；本地校验成功不等于远程上传成功。

重要：本包不会自动覆盖Markdown文档，也不会在未输入Y时提交或推送。
