"""Render editable vector overlays over the unchanged approved plan; no AI generation."""
from pathlib import Path
import base64
import hashlib
import html
import json
import math

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
PLAN = PROJECT / 'assets/space/PLAN-001_彩平图_20261025_阳台家具删除版.png'
BG = base64.b64encode(PLAN.read_bytes()).decode()
COL = {'a':'#1463dc','b':'#ad35bb','cat':'#db7600','cam':'#d22b45','eye':'#078271'}
G = (230, 525, 663, 805)
A = (620, 675)
E = (232, 565)
X = (663, 720)

def label(x, y, text, color='#183046', size=16):
    width = sum(size * (0.58 if ord(c)<128 else 1) for c in text) + 14
    return f'<g><rect x="{x-5}" y="{y-size-3}" width="{width}" height="{size+10}" rx="4" fill="white" fill-opacity=".94"/><text x="{x}" y="{y}" fill="{color}" font-size="{size}">{html.escape(text)}</text></g>'

def path(points, color, dash=False, width=4, arrow=True):
    coords = ' '.join(f'{x},{y}' for x,y in points)
    attrs = 'stroke-dasharray="9 7"' if dash else ''
    tip = f'marker-end="url(#{color[1:]})"' if arrow else ''
    return f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {attrs} {tip}/>'

def actor(pos, text, key='a'):
    x,y=pos; c=COL[key]
    return f'<circle cx="{x}" cy="{y}" r="15" fill="white" stroke="{c}" stroke-width="3"/><text x="{x}" y="{y+5}" text-anchor="middle" font-size="15" font-weight="700" fill="{c}">{text}</text>'

def camera(pos, target, name, dx=10, dy=-16, low=False):
    x,y=pos; tx,ty=target; c=COL['cam']; angle=math.degrees(math.atan2(ty-y,tx-x))
    # Direction-only wedge: not a calibrated field of view or a metric clearance.
    fan=f'<path d="M{x},{y} L{x+120*math.cos(math.radians(angle-18))},{y+120*math.sin(math.radians(angle-18))} L{x+120*math.cos(math.radians(angle+18))},{y+120*math.sin(math.radians(angle+18))} Z" fill="{c}" opacity=".10"/>'
    return fan+path([pos,target],c,True,2)+f'<g transform="translate({x},{y}) rotate({angle})"><rect x="-9" y="-7" width="17" height="14" rx="2" fill="{c}"/><path d="M8,-5 L17,-10 L17,10 L8,5Z" fill="{c}"/></g>'+label(x+dx,y+dy,name+(' 低位' if low else ''),c,14)

def base(title, subtitle):
    defs=''.join(f'<marker id="{c[1:]}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8Z" fill="{c}"/></marker>' for c in COL.values())
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1760" height="1160" viewBox="0 0 1760 1160"><defs>{defs}</defs><style>text{{font-family:"Microsoft YaHei","Noto Sans CJK SC",sans-serif}}.h{{font-weight:700}}</style><rect width="1760" height="1160" fill="#f3f5f7"/><text x="45" y="54" font-size="31" class="h" fill="#152f45">{title}</text><text x="45" y="89" font-size="18" fill="#526676">{subtitle}</text><text x="45" y="124" font-size="17" fill="#526676">蓝=A妻子　紫=B妻子　橙=布布　红=已批方案机位　绿虚线=视线　橙虚线=跳跃　G虚框仅供制作、成片无边界特效</text><svg x="45" y="155" width="1670" height="530" viewBox="0 390 1420 450"><image href="data:image/png;base64,{BG}" width="1672" height="941"/><rect x="230" y="525" width="433" height="280" fill="#38c5c7" fill-opacity=".09" stroke="#138b96" stroke-width="3" stroke-dasharray="10 7"/>{label(245,548,'G方案范围：非实测','#137985',15)}{actor(E,'E','cat')}{actor(X,'X','cat')}'''

def finish(content, notes, name):
    content+='</svg>'
    for i,(heading,body) in enumerate(notes):
        y=746+i*85
        content+=f'<text x="50" y="{y}" font-size="20" class="h" fill="#17354a">{html.escape(heading)}</text><text x="50" y="{y+30}" font-size="18" fill="#40566a">{html.escape(body)}</text>'
    content+='<text x="50" y="1132" font-size="16" fill="#aa4a23">状态：2026-10-25用户批准机位与路线V1｜不代表实测净距/三维遮挡/动态验收｜基底PLAN-001，侧视VIEW-03采用v02</text></svg>'
    (HERE/f'{name}.svg').write_text(content,encoding='utf-8')

def build():
    HERE.mkdir(parents=True,exist_ok=True)
    s=base('SC04｜先发现家变了，再看到布布，最后经过E进入G','剧情时间22:58—23:15；摄影机编号是验证机位，不等于最终镜头数。图左=阳台，图右=餐厨，无地理北向假定。')
    s+=actor(A,'A')+actor((620,696),"A′")+path([A,(620,696)],COL['a'],False,3)
    s+=path([A,(145,530)],COL['eye'],True,2)+path([A,(615,450)],COL['eye'],True,2)
    s+=actor((145,535),'猫','cat')+path([(145,535),(190,555),E,(320,565),(495,565),(555,605)],COL['cat'])
    s+=camera((710,550),A,'C41 人物反应',15,-15)+camera((330,505),E,'C42 越E',-85,-17,True)
    s+=label(55,496,'B猫爬架：G外候选区',COL['cat'],14)+label(505,422,'B食水区：G外',COL['eye'],14)
    s+=label(350,588,'23:14 四脚依次越E',COL['cat'],14)+label(515,635,'23:15 停住后回应',COL['cat'],14)
    finish(s,[('① 守候与异变','A站在沙发餐厨端的G内；只朝扶手方向退小半步。先转头看猫爬架及食水区，再看到猫影。'),('② E进入路线','23:13猫仍在G外且不回应；经开放阳台垭口走到沙发窗端前方，23:14四脚全入G，23:15才回应。'),('③ 摄影与视线','C41固定拍人物反应；猫用品以A眼位附近的视线插镜覆盖；C42低位单独证明越E，不把数个动作塞进一镜。'),('④ 尚待验证','VIEW-01和新版VIEW-03支持开放垭口、外窗关闭；G边界属相对转绘，精确开口宽度、退步余量仍需关键帧核验。')],'SC04_camera-route_v1')

    s=base('SC05｜从生活痕迹到真实触碰；地面行走与跳跃分开标注','剧情时间23:16—23:23；妻子不追猫穿过窄缝，布布先按习惯活动，再主动靠近。')
    s+=actor(A,'A')+actor((555,605),'1','cat')
    s+=path([(555,605),(565,660),(565,700)],COL['cat'])
    s+=path([(565,700),(555,745)],COL['cat'],True)+path([(555,745),(365,745),(302,700),(302,650)],COL['cat'])
    s+=path([(302,650),(430,650)],COL['cat'],True)+path([(430,650),(505,675)],COL['cat'])
    s+=path([(505,675),(550,703)],COL['cat'],True)+path([(550,703),(595,690),(608,685)],COL['cat'])
    s+=actor((302,650),'2','cat')+actor((430,650),'3','cat')+actor((550,703),'4','cat')
    s+=camera((700,560),(410,700),'C51 习惯动作',0,-15)+camera((750,700),A,'C52 接触抱猫',15,30)
    s+=label(245,612,'扶手旁特定浅褶：SC07保留',COL['cat'],13)
    finish(s,[('① 行为顺序','1回应后→沿茶几餐厨侧绕到沙发→2踩薄毯/擦抱枕→3跳上茶几碰遥控器→4落砖→闻手、蹭手、被抱。'),('② A连续蹲姿已批','23:15蹲稳后原位观察，23:21同一蹲姿伸手；23:23先托猫抱稳，再抱猫起身站稳，衔接SC06。'),('③ 摄影与剪接','C51覆盖猫与物件关系，动作拆为可核验的局部；C52拍接触与抱起。跨机位以猫所在家具和朝向校验，不凭地图保证轴线。'),('④ 不能当成已验证的部分','橙虚线是已批路线中的跳跃，不是猫穿家具；高差、跳距、承重点及人手托猫仍需少量关键帧验证，不能据图直接开视频任务。')],'SC05_camera-route_v1')

    s=base('SC06｜双妻子可见性、放手与X返程','剧情时间23:24—23:30；A与布布在G内，B始终在G外。主观空镜取自B真实眼位。')
    s+=actor(A,'A')+actor((820,620),'B','b')+actor((780,720),"B′",'b')
    s+=path([(1090,605),(950,605),(820,620)],COL['b'])+path([(820,620),(855,670),(820,715),(780,720)],COL['b'],True,3)
    s+=path([A,(820,620)],COL['eye'],True,2)+path([(820,620),A],COL['eye'],True,2)
    s+=path([(620,690),(645,715),X,(735,720)],COL['cat'])+actor((735,720),'猫','cat')
    s+=camera((535,540),(750,650),'C61 客观关系',-100,-15)
    s+=camera((820,620),A,'C62=B眼位',15,-35)
    s+=camera((740,515),(665,718),'C63 放手/越X',15,-15,True)
    s+=label(950,576,'B由厨房出来',COL['b'],14)+label(755,777,'B转身发现→蹲下抱回',COL['b'],14)
    finish(s,[('① 客观与主观是两个位置','C61在G靠电视一侧朝餐厨斜拍，尝试前景A抱猫、后景B寻猫；C62就在B眼位，向同一沙发区看去：只有家具，没有A和猫。'),('② B的搜寻与可见性','B沿G外餐厨通道走近、侧移、弯腰看茶几下；脚不跨G。她看的是家具区域，不与A形成眼神交流。'),('③ X返程的完整因果','23:29 A在G内蹲下放猫、手松开→猫完整越X→B转身自然发现并抱起；23:30交汇才关闭。A留在原位不追。'),('④ 优先核验','C61下半身可能被茶几遮挡，不能据平面线认定全身可见；C62不等于C61原位删人。X地面无柜体穿插，但实际净距未实测。')],'SC06_camera-route_v1')
    metadata={'date':'2026-10-25','status':'director_approved_plan_dynamic_unverified','base_image':str(PLAN.relative_to(PROJECT)),'base_sha256':hashlib.sha256(PLAN.read_bytes()).hexdigest(),'view03_sha256':hashlib.sha256((PROJECT/'assets/views/VIEW-03_朝沙发.png').read_bytes()).hexdigest(),'coordinate_system':'PLAN-001 image pixels, x right/y down; no metric calibration','G_candidate':[230,525,663,805],'A_candidate':A,'E_candidate':E,'X_candidate':X,'B_search_candidate':[820,620],'B_retrieve_candidate':[780,720],'mapping':'PLAN-002 boundary relationships visually transferred to current PLAN-001; not surveyed registration','scene_routes':{'SC04':[[145,535],[190,555],list(E),[320,565],[495,565],[555,605]],'SC05_walk_to_sofa':[[555,605],[565,660],[565,700]],'SC06_X':[[620,690],[645,715],list(X),[735,720]]},'validation_limits':['2D topology only; physical width/height/occlusion not certified','camera wedges are directions, not calibrated lens cones','camera/route plan approved 2026-10-25; metric placement and 3D framing remain unverified'],'paid_generation':False}
    assert all(G[0]<x<G[2] and G[1]<y<G[3] for x,y in [A,(620,696),(620,690),(608,685)])
    assert all(x>G[2] for x,y in [(1090,605),(950,605),(820,620),(855,670),(820,715),(780,720)])
    assert metadata['scene_routes']['SC06_X'][-1][0]>G[2]
    furniture=[(240,710,600,795),(240,615,335,795),(380,605,510,695),(700,755,880,795),(240,420,665,465)]
    cameras=[(710,550),(330,505),(700,560),(750,700),(535,540),(820,620),(740,515)]
    assert all(not(x0<x<x1 and y0<y<y1) for x,y in cameras for x0,y0,x1,y1 in furniture)
    metadata['camera_points']=dict(zip(['C41','C42','C51','C52','C61','C62','C63'],cameras))
    metadata['checks_passed']=['A and retreat/release markers inside candidate G','B search/retrieve markers outside candidate G','cat X endpoint outside candidate G','camera points outside approximate plan-view furniture footprints']
    (HERE/'coordinates-and-validation.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    names=['SC04_camera-route_v1','SC05_camera-route_v1','SC06_camera-route_v1']
    articles=''.join(f'<article id="{i}"><h2>{n[:4]}</h2><img src="{n}.svg" alt="{n}机位与运动路径预演图"><p><a href="{n}.png">下载PNG</a> · <a href="{n}.svg">打开可缩放SVG</a></p></article>' for i,n in enumerate(names))
    (HERE/'index.html').write_text('''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>布布 SC04—SC06 机位与路线候审</title><style>body{margin:0;background:#eef2f5;color:#19354a;font-family:Microsoft YaHei,sans-serif}header,main{max-width:1600px;margin:auto;padding:24px}header{background:white}h1{font-size:28px}p{line-height:1.7}a{color:#1463dc;margin-right:12px}article{margin-bottom:36px;background:white;padding:15px;border-radius:12px}img{display:block;width:100%;height:auto}nav{position:sticky;top:0;background:#fff;padding:12px;z-index:2}</style><header><h1>《另一个家的布布》SC04—SC06 机位与运动路径预演 V1</h1><p>空间母版与行动规则沿用已确认资料；机位与路线方案已获用户批准，实测与动态仍待验证。图层未重生成装修，原始母版未改动。新版VIEW-03已作为侧视依据。</p><p>此为二维机位/路线预演，不是人物关键帧或动态视频；扇形只表方向，不代表标定视锥。</p></header><main><nav><a href="#0">SC04 异变与进入</a><a href="#1">SC05 习惯与重逢</a><a href="#2">SC06 放手与返回</a><a href="README.md">验证结论/待确认</a></nav>'''+articles+'</main></html>',encoding='utf-8')

if __name__=='__main__':
    build()
    print('3 SVG boards + HTML review + coordinate checks created')
