# v07｜用户授权的局部图层合成

用户认可局部工作图的毛质、否决全身v06的回填结果，并明确同意常规图层合成。本轮不调用生成模型。

底图：`../assets/K05-H1_v03.png`。毛质源：`../assets/fur-detail_v06_working.png`。源文件不覆盖。工作图只授权用于毛质，不以它重绘猫脸或人物。

`build_composite.py`读取`alignment.json`，按0.29比例Lanczos缩放源图，位移对齐，在人工选取的胸肩/腹侧毛区应用透明蒙版。肤色排除和明确手部保护避免来源手位差异带入；头部保护至y=200。羽化只发生在蒙版内部，禁止影响外侧像素。毛层在`fur-layer.png`，蒙版在`fur-mask.png`，对照在`before-after.png`。

复现：在本仓库执行 `python projects/另一个家的布布/scene-keyframes/SC05/K05-H1/composite-v07/build_composite.py`。只需已有Pillow和numpy，未安装软件或修改环境。

像素自检见`verification.json`：原图大小不变，蒙版外变化为0，定义的头脸/双手保护区变化为0，实际毛区有2439个像素发生变化。此结果证明合成范围受控，不代替审美和接缝验收。

最终图：`../assets/K05-H1_v07.png`，待用户审核。源图缩小会损失细节，不声称小幅全景与局部大图可有相同毛发辨识度；手边/颈部边缘仍保留部分底图毛，未用锐化伪造细节。未生成视频，未改变光影或构图。
