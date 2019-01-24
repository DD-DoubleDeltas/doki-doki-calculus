# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define daye  = Character('박다예',color="#ffffff")
define dasuk = Character('민다석',color="#ffffff")
define chime = Character('이차임',color="#ffffff")
# 여기에서부터 게임이 시작합니다.

label start:
    #장면 : 교실
    call dev_select_call
    "딩동댕동"
    dasuk "으아- 드디어 시험 끝났다!"
    "사흘 간 몰아치던 긴장감이 방금의 종소리로 순식간에 허무하게 사라졌다."
    "해방감과 피로에 젖어있을 무렵, 누군가가 내 자리를 향해 걸어오는 것이 들렸다."
    show chime default at center:
        xalign 0.7
    chime "드디어 끝이네!"
    chime "시험은 잘 봤니?"
    hide chime
    dasuk "나 국어 망했는데..."
    show chime default
    "내 앞에 서 있는 얘는 이차임. 인미고등학교 2학년"
    "나와 같은 반인, 소꿉친구다."
    "뭐, 이렇게 시험 끝난 날에는 잘했는지, 망했는지, 서로 안부를 묻고는 한다."
    chime "너, 이번 수학은 잘 봤냐?"
    hide chime
    "수학이라, 내 가채점 결과는 87점인데..."
    menu:
        "잘 봤어.":
            call start_sub1_1
        "망했어.":
            call start_sub1_2
        "잘 망했어.":
            call start_sub1_3
    show chime default
    chime "같이 숙제할 때 봤는데, 너 외워서 하는것 같던데?"
    hide chime
    "틀린 말은 아니다. 공식은 당연히 외웠고, 학습지에 나온 패턴들을 모조리 외워서 이 점수인 것이다."
    dasuk "메모리에 올려두고 연산을 줄이는 것도 꽤나 좋은 기법이란다."
    "수학을 암기로 푼다는게 자랑할 거리는 아닌 것 같지만."
    "일부러 유식한 척 티를 내본다. 이러면 보통 극혐하면서 떨어져 나가니깐."
    show chime default
    chime "후후, 그치? 너정도 머리되는 애면 연산도 꽤나 잘 할것 같구..."
    "...변수가 생겼다."
    "오늘따라 차임이가 유난히 내 옆에 붙어오며 치근댄다."
    "소꿉친구로써 이런 반응을 보이는 이유를 모를 리는 없다."
    "최소한 무슨 속셈이 있어서 저런 거겠지."
    "반응을 보아하니, 학원에서 오답풀이라도 시켰나보다. 대신 해달란 거겠지."
    hide chime
    "당연하겠지만, 귀찮다."
    "시험도 끝난 마당에 더 이상 수학 문제를 보긴 싫다."
    "수학이 싫지 않다 해도, 체력이 달린다."
    "차임이에게 최대한 자연스럽게 거절하려면..."
    menu:
        "됐고, 집에 갈꺼야.":
            call start_sub2_1
        "알았어, 그럼 나중에...":
            call start_sub2_2
        "return 0;":
            call start_sub2_3

    #장면 : 하교길
    "집에 가는 길은 정말 애매하다."
    "버스를 타기에는 너무 가깝다."
    dasuk "몇 정거장 갈 바에야... 택시를..."
    "잡고 싶지만 안 잡힌다"
    dasuk "콜택시 부르기는 귀찮고, 돈도 아깝고..."
    "그럼 걸어야지."
    dasuk "전혀 애매하지 않군"
    "그런 생각을 하며 오늘도 집으로 간다."
    dasuk "흠.. 오늘도 같은 길로 가나?"
    "항상 나와 같은 하교길을 가는 여자애가 있다."
    show daye default
    "저 흑발에 긴 머리."
    "어떤 날은 내가 앞서가고, 어떤 날은 그녀가 앞서 간다."
    "오늘은 그녀가 나를 앞서 간다. 내가 늦게 나온 탓이다."
    "매번 봐서 그런지 별로 신경 쓰이진 않는다.
    hide daye
    "......"
    "......"
    "나는 거의 같은 속력으로 움직이고 있다."
    "길을 x축이라 했을 때 v, 즉 dx/dt가 거의 일정하다는 거지."
    dasuk "이걸 기억하고 있군."
    "나는 보통 시험을 치면 그에 관한 기억이 바로 포맷된다."
    "그런데 이것을 기억하고 있구나."
    "굉장히 의아하다는 생각을 하며 나는 계속 걸어갔고,"
    "???" "아얏!"
    show daye default
    "내가 정신이 팔려있던 사이, 어느새 그녀와의 거리가 0이 되어 충돌했다."
    "별로 세게 부딪히진 않았지만 등 뒤에서 누군가가 툭 하고 닿으니 분명 놀랐을 것이다."
    dasuk "아, 미안!"
    "재빨리 사과한다. 괜스레 미안해진다."
    show daye default
    "???" "민다석."
    dasuk "아... 박다예?"
    show daye default
    "???" "민다석."
    dasuk "아... 박다예?"
    "출석번호상 바로 나 다음인데, 이름 정도는 알고 있다."
    "수학과 과학에 있어서는 상위권을 놓치지 않는 그녀."
    "국어나 영어는... 글쎄?"
    daye "이제 알았냐? 눈을 어디다 뜨고 다니는거야!"
    hide daye
    dasuk "미안... 한 눈이 팔려서."
    "날카로운 말투로 무섭게 쪼아댄다."
    "기가 눌린 채 변명 아닌 변명을 하게 된다."
    show daye default
    daye "아니, 나와 거리가 0으로 근접하는 것을 알았으면 멈춰야 할 거 아냐?!"
    "......"
    "'역시 그 수학 머리는 어디 가지 않나보다?'라고 태클이라도 걸고 싶지만"
    "지금 다예의 심기를 건드리는 건 좋은 생각이 아닌 것 같다."
    show daye default
    daye "흐음..."
    "다예가 풀이 죽은 나를 쭉 훑어보더니,"
    daye "마침 잘 됐네. 너 운 좋은 줄 알아."
    hide daye
    "몇 마디 던지고 나선 등을 돌린다."
    "다행이다. 별 탈 없이 넘어가는 것 같다."
    daye "자율동아리를 만들 건데, 들어오면 부딪힌 것 정도는 용서해줄께."
    dasuk "......"
    "별 탈 없이 넘어가는 게 아니었다."
    "하아... 귀찮지만..."
    show daye default
    daye "뭐야, 불만 있어?"
    "다시 뒤로 돌아 나를 날카로운 눈빛으로 쳐다본다."
    hide daye
    "그래, 뭐... 대충 하면 되겠지."
    "하아..."
    
    chime "흐음... 다석아? 하자?"
    dasuk "넌 또 언제 온거야!!"
    daye "오! 안녕 차임아!"
    chime "그럼! 아는 사이지!"
    dasuk "호오..."
    daye "호오..가 아니잖아!!"
    chime "어차피 쟤 딱히 상관없어"
    dasuk "잠깐 당사자 의견..."
    chime "(찌릿)"
    dasuk "......."
    "......"
    chime "암기로 수학시험을 치는 너의 나쁜 습관을 해결하기 위해 미적분 학습 동아리를 만들 예정이란다"
    dasuk "하아...."
    daye "흐음...."
    dasuk "아아아...."
    
    #장면 전환(주인공의 집)
    ##메신저 그림
    dasuk "하아...머리야"
    "결국은 동아리 가입을 승낙하였다."
    dasuk "음? 지금 나에게 연락할 사람이 누가 있지?"
    "연락할 사람 딱히 없는데? 뭐지?"
    dasuk "아..."
    "다예 : 동아리 명은 '미적분의 이해"
    "차임 : 오오 멋져"
    "다예 : 내일 방과후부터 바로 활동 시작할거야"
    "다석 : 아아아아 시험 오늘 끝났잖아..."
    "다예 : 미분해줄까?"
    "차임 : 사람을 미분한다니...와..."
    "다석 : ㅈㅅ"
    "다예 : 그래서, 너는 어디까지 이해하고 있니"
    dasuk "아 잠만....."
    "다석 : 미적분 한정으로 전부다 까먹었..."
    
    "휴대폰" "전화받아라 위윙위웅윙"
    dasuk "....."
    "다예 번호인데"
    "불안하게, 뭐지?"
    dasuk "여보...."
    daye "극한부터 시작한다. 책 들고와"
    dasuk "...네"
    "하아...앞날이 깜깜하다...."
    jump chapter_1_1_intro


label start_sub1_1:
    dasuk "잘 쳤어."
    show chime default
    chime "오, 그래? 몇 점인데?"
    hide chime
    dasuk "87점."
    show chime default
    chime "오~ 생각보다 잘 쳤는데에!"
    "차임이는 내 점수를 듣고는 약간 비꼬는 투로 말한다."
    "아무래도 차임이는 나를 과소평가했던 것 같다."
    hide chime
    dasuk "나 수학 원래 잘 하는데?"
    show chime default
    chime "거짓말 하지 마~!"
    hide chime
    return
    
label start_sub1_2:
    dasuk "망했어."
    show chime default
    chime "흐음... 괜찮아, 몇 점인데 그래?"
    hide chime
    dasuk "87점."
    show chime default
    chime "뭐야, 잘 쳤는데? 이게 망했다구?"
    "분명 자신감이 없었지만, 차임이는 의외라는 듯 되려 놀라고 있다."
    hide chime
    dasuk "하... 아깝다. 하나만 더 맞으면 2등급도 노려볼 수 있는데."
    show chime default
    chime "너 주제에 그 정도면 잘 한거지~ 뭘 더 바래?"
    hide chime
    "어쭈, 저게 놀리고 있네."
    return
    
label start_sub1_3:
    dasuk "잘 망했어."
    "내가 말했어도 무슨 소리인가 싶다."
    show chime default
    chime "뭐야, 그 애매한 대답은...? 그래서 몇 점인데 그래?"
    hide chime
    dasuk "87점."
    show chime default
    chime "으음... 잘 치지도 못 치지도 않은 애매한 점수?"
    hide chime
    dasuk "그렇지."
    show chime default
    chime "푸흐, 너 한테 딱 맞는 점수 아냐?"
    hide chime
    return
    
label start_sub2_1:
    dasuk "됐고, 집에 갈꺼야."
    "이런 부탁일수록 확실히 뿌리쳐야만 한다."
    "아니면 차임이는 내 말을 무시하고 계속 늘어질 게 뻔하다."
    show chime default
    chime "칫, 쪼잔하긴."
    dasuk "수작 부리지마. 너한테 속은 게 한두 번이었어야지."
    hide chime
    "차임이는 나한테 대놓고 불만스러움을 드러내고 있다."
    "뭐, 어쩌라고. 나도 휴먼이야, 휴먼!"
    "...차임이는 무시하고, 집으로 돌아가기로 했다."
    return

label start_sub2_2:
    dasuk "하... 알았으니깐 그럼 나중에..."
    show chime default
    chime "역시 눈치가 빨라! 나중에 해주겠단 거지!?"
    hide chime
    "이런."
    "차임이의 눈동자가 반짝반짝하고 빛나는 것 같다."
    show chime default
    chime "그럼, 이거 5시까지 부탁해!"
    hide chime
    "자기 멋대로 일정까지 다 잡아놓는다."
    "이래서 휘말리게 되면 엄청 귀찮아진다."
    "안 하면 더 귀찮아 진다. 빨리 끝내놓자."
    return

label start_sub2_3:
    dasuk "'return 0;'"
    "리턴 제로."
    "만약 이 세상이 누군가의 시뮬레이션이라면, 이걸로 이 상황을 빠져 나올 수 있을 것이다."
    show chime default
    chime "응? 뭐라고 했어?"
    "아까 전의 터무니없는 소리를 들은 차임이가 당황한다."
    "혹시나 했던 망상일 뿐이지만, 그게 아니면 이 세상은 C언어 계열이 아닌 것 같다."
    "...됐고, 차임이가 멍 때리는 사이 어서 학교를 빠져나가자."
    return
    
#챕터1, 극한
label chapter_1_1_intro:
    dasuk "...그래서 일단 책을 들고 왔어"
    chime "다석이가 시험기간이 아닐 때 책을 들고 있네"
    dasuk "외울 때가 아니면 책을 볼 필요가 딱히 없으니까"
    daye "찌릿"
    call dev_select_call
    "다예가 나를 째려본다"
    dasuk "...그래서 오늘은 극한이라고?"
    daye "응. 수열의 극한과 함수의 극한에 대하여 설명할 거야"
    dasuk "극한... 뭐였지"
    chime "흐음... 우선 극한이 뭔지부터 설명해줘야 할것 같기도 하고"
    daye "....극한을 어디다가 쓸 수 있는지부터 말해줘야 하지 않을까? 일단 극한의 발명 역사는 나도 잘 몰라..."
    chime "개인적인 의견이지만, 미분이나 적분이 없으면 극한이란건 우리가 접할 일이 없다고 생각해"
    dasuk "흐음? 적어도 우리에게는 극한은 뭔가 필요해서 배우고 가는 느낌이라는것 같은데"
    daye "실제로는 잘 모르겠어. 극한 자체로도 꽤나 중요하고 흥미로운 수학적 대상이지만"
    chime "...고등학교 미적분에서 다루기는 어려워"
    dasuk "그래? 그럼 미분이 왜 필요한지 설명이 필요한데"
    daye "공이 떨어진다고 생각해보자"
    show expression "chapter-1-1-pic-1.png" as pic at truecenter
    "다예가 그림을 그렸다"
    dasuk "이 화살표는?"
    chime "...공기저항?"
    daye "그렇지"
    daye "공기저항, 즉 공의 속력 감소가 공의 속력에 비례한다면"
    daye "낙하 시작 후 시각에 따른 공의 속력은?"
    chime "흐음...꽤나 괜찮은 문제인데"
    dasuk "....으음..."
    dasuk "그러니까, 속력 변화와 속력이 들어가 있는 문제잖아"
    "흐음..."
    daye "그리고 하나 알아두어야 할 것"
    daye "미분이라 함은"
    chime "...변화량이다!"
    daye "나중에 미분을 배울 때 다시 말해주겠지만, 미분은 어떤 함수의 변화량을 알 수 있는 도구라고 생각하면 편해"
    dasuk "속력의 변화라 하니까 미분이 뭔지 알아야 겠는데. 그런데 극한과 무슨 관계가 있지?"
    hide pic
    chime "...우리 시험범위에 도함수의 정의가 있었는데, 진짜 다 까먹었나 보네"
    daye "...평균변화율이 뭔지 알아?"
    dasuk "으음...x가 h만큼 변할때 f의 변화를 h로 나눈거"
    scene expression "chapter-1-1-eq-1.png" as eq at truecenter
    chime "그러니까, 이렇게"
    "차임이가 식을 하나 적었다."
    dasuk "그런데 왜?"
    daye ".....있잖아, 평균변화율의 단점이 뭔줄 알아?"
    dasuk "????"
    chime "예를 들어 t=1초부터 t=1.5초까지의 평균변화율은 알 수 있지만"
    daye "t=1초때의 순간적인 변화율은 알 수 없어"
    dasuk "굳이 알아야 하나?"
    daye "...미분은 특정 순간에서의 변화율을 측정하는것. 평균변화율만으로는 정확한 값을 알 수 없어."
    dasuk "흐음.. 그런데 저기서 만약에 h를 0가 0이 아닌, 0으로 접근시키고"
    "분모가 0이 될 수는 없으니까, 0이라고 하기 보다는 0에 접근시키는 것이다.  대입이 아니니까 수학적 오류는 없겠지"
    dasuk "그 때, 저 평균변화율 식이 어떤 값에 가까워진다면, 그것을 사용하면 문제가 없을것 같은데?"
    chime "오호?"
    "h를 0에 한없이 가깝게 접근시키면 사실상 순간적인 변화율이 될 것이다."
    daye "잘 생각했는데 '한없이 접근시키는것'이 극한이야"
    hide eq
    call dev_select_call
    chime "너가 방금 말한 h를 0으로 접근시킨 평균변화율은 나중에 순간변화율이라 다시 나오겠지만"
    chime "식으로 쓰면 이렇게...."
    show expression "chapter-1-1-eq-2.png" as eq at truecenter
    dasuk "흐음? lim?"
    daye "limit, 리미트, 리밋. 마음대로 읽어. 극한이라는 뜻이고 밑에 h를 0으로 보낸다는 이야기야"
    chime "..허허 어쩌다 보니 함수의 극한이 나왔네?"
    dasuk "뭐부터 해야 했던 거야?"
    daye "으음, 고등학교에서는, 수열의 극한부터 하는 것이 미적분I의 배치로 알고 있는데"
    chime "미적분 II는 미적분I 이수를 전제로 하니 패스"
    hide eq
    daye "그래서 이렇게 극한의 필요성에 대한 설명이 끝났는데, 질문 있니?"
    $middle_edu = 0
    $high_edu = 0
menu:
    "딱히 없는것 같아.":
        jump chapter_1_1_outro
    "한없이 다가간다?":
        $ high_edu += 1
        dasuk "저기 lim기호 보고 생각난건데"
        show expression "chapter-1-1-eq-3.png" as eq at truecenter
        chime "응?"
        dasuk "생각해보니 일단 저거 h에 0을 대입한다는것은 아니잖아"
        chime "그렇지"
        dasuk "그런데 그냥 0으로 접근하다 보면 0을 대입하게 되는거 아냐..?"
        "뭔가 표현이 애매하다"
        dasuk "한없이 가까워진다는 표현도 조금 애매하다고 생각해"
        daye "좋은 지적이야. 사실, 이 부분은 이전의 수학자들에게도 지적된 부분이기는 해"
        dasuk "앵?"
        daye "...이 부분은 고등학교 레벨에서는 다루지 못하게 되어 있어. 대학교 레벨이라는 거야"
        chime "오?"
        hide eq
        daye "궁금하면 해석학에 대해서 스스로 검색 정도만 해봐."
        dasuk "흐음..."
        daye "참고로 이거 무시해도 고등학교에서는 논리 전개에는 문제가 없어"
        dasuk "오호, 그럼 일단 넘기는걸로"
        chime "그런걸로!"
        jump chapter_1_1_outro
    
label chapter_1_1_outro:
    chime "어우야, 이제 조금 쉬었다가 하는게 어때?"
    daye "겨우 이정도 가지고?"
    dasuk "조금 쉬는게 좋다고 생각하는데"
    daye "솔직히 말해서 개발자 입장에서는 코드 1백줄도 안지난...."
    "개발자" "어이. 그냥 쉬어라. 극한 1장 아웃트로라고. 쉬다해 좀!!"
    chime "그렇다고 하네"
    dasuk "갑자기 개발자가 튀어나오는구만"
    daye "어이, 미연시에 개발자가 갑툭튀하면 분위기 깬다고!!"
    "개발자" "(도망)"
    daye "...그래 지금까지 극한의 필요성에 대하여 설명하였고"
    chime "함수이 원판이라 할 수 있는 수열의 극한에 대하여 설명할거야"
    dasuk "...왜 하필 수열부터 시작하는 거야?"
    chime "...자연수를 배우고 실수를 다루는것과 같은 원리?"
    dasuk "흐음...그래?"
    daye "교육적으로 그렇다는 말은 못들었는데, 꽤나 그럴듯하게 들리는데"
    chime "크흠"
    dasuk "그럼 조금 쉬었다가 하자!"
    #배경화면 복도
    "복도로 나왔다"
    "머리를 식힌다"
    dasuk "아직까지는 할만하군"
    if high_edu > 0:
        daye "흐음? 아직 아무것도 시작하지 않았거든?"
        dasuk "히익!!! 놀래라!!"
        daye "뭘 그렇게 놀래냐"
        dasuk "등 뒤에서 그렇게 급습하면 간이 0으로 가는것 같단 말이다!!"
        daye "....푸흡"
        dasuk "...왜?"
        daye "간떨어질뻔 했다는것을 그렇게 표현하네"
        daye "...푸흡"
        dasuk "그러게 말이다."
        daye "푸흡..하여튼 5분 뒤에...푸흡"
        dasuk "..."
        daye "차임이가 수열의...푸흡...극한 설명 시작하니까"
        dasuk "......."
        daye "시간맞춰 들어와...푸흡..끄끅"
        "다예가 문을 닫고 들어갔다"
        dasuk "해석학이라...."
        "검색을 해보았다"
        "해석학(analysis):대수학과 기하학에 대하여, 미분과 적분을 기초로 함수의 연속성에 관한 성질을 연구하는 수학의 분야이다"
        dasuk "미분적분학을 엄밀하게 형식화 하는 것을 목적으로 시작된 수학의 한 분야라..."
        "적어도 지금 다룰것은 아니군"
        dasuk "일단 끄고"
        "화장실이나 들렀다가 들어가도록 하자..."
        jump chapter_1_2_intro
    else:
        chime "다행이네"
        dasuk "꾸애액"
        chime "꺄아아아악"
        dasuk "놀랬잖아!!"
        chime "히히"
        dasuk "뭐가 히히냐"
        chime "...5분 뒤에 들어오라는걸 전해주려 왔어"
        dasuk "흠..그래?"
        chime "그런거야"
        "잠시 눈이 마주쳤다"
        "......"
        "......"
        dasuk "......"
        chime "......"
        dasuk "......"
        chime "......"
        daye "......둘이 무슨 사이?"
        dasuk "꾸애애액!"
        chime "꾸애액!!"
        daye "1분 남았다. 얼른 마무리 하고 들어와"
        chime "뭘 마무리 하라는거야!!"
        dasuk "너가 생각하는 그런거 아니거든?"
        daye "흐음? 눈만 바라보는 관계가 아니라면 어디까지 간거야?"
        dasuk "꾸액"
        chime "다예야? 맞을래?"
        daye "히히히히히히"
        "대략 55초 만에 사태가 진정되었고"
        "수열의 극한에 대한 차임이의 설명을 듣게 되었다"
        jump chapter_1_2_intro
    
label chapter_1_2_intro: #수열의 극한-수렴과 발산
    #다시 동아리실 배경
    dasuk "수열의 극한이라..."
    call dev_select_call
    daye "수열에 대해서 기억하니?"
    chime "과연?"
    dasuk "수의 나열"
    chime "딱히 틀린말은 아닌것 같은데"
    daye "...고등학교에서 수열의 정의를 어떻게 하고 있는지는 모르겠지만, 자연수집합에서 실수집합으로 가는 함수라고 보렴..."
    "꽤나 적당한 정의군"
    chime "우선 가장 간단한 예시부터 볼까?"
    show expression "chapter-1-2-0-eq-1.png" as eq at truecenter
    daye "일단 이 식의 의미가 뭔지 말해봐"
    dasuk "어디보자, 우선 n이 무한대로 '간다'고 되어 있네"
    "즉 n을 계속 크게 하겠다는 소리이다."
    dasuk "그때의 1/n을 의미하는 건데"
    hide eq
    chime "값이 존재할까?"
    dasuk "흐음...."
    "우선 1/n은 n이 커질수록 작아진다. n=1일때를 생각하면 1이다"
    "그리고 1/n은 반드시 0 이상의 값을 가진다"
    "그리고 n을 계속 크게 하다보면, 0에 가까워진다고 생각할 수 밖에 없다"
    if high_edu > 0:
        "만약, 0 이외의 양수에 가까워진다고 가정한다면, n을 충분히 크게 하면 그 양수보다 작은 1/n이 있거든"
        "개발자" "정확한 것은 아르키메데스 정리를 검색해보세요!"
    show expression "chapter-1-2-0-eq-2.png" as eq at truecenter
    dasuk "엄밀하게 증명은 못하겠는데 0 인것 같다."
    chime "정답"
    daye "엄밀하게 증명하는 것은 아까 말했지만 미적분학 레벨이 아니므로 생략!"
    dasuk "흐음.. 왠지 이게 굉장히 중요했던 것으로 기억하는데.."
    chime "그렇지. 중요하지"
    hide eq
    chime "그러면 이건 어때?"
    show expression "chapter-1-2-0-eq-3.png" as eq at truecenter
    dasuk "응?"
    "계속 키우는 마당에 n이나 n+2나 똑같을것 같은데"
    hide eq
    daye "..."
    dasuk "0"
    daye "이런걸 두고 '수렴한다'고 하는거야"
    dasuk "흐음? 그러면 수렴하지 않는 것도 있다는 거잖아?"
    daye "당연하지"
    chime "예를 들면..."
    call dev_select_call
    show expression "chapter-1-2-0-eq-4.png" as eq at truecenter
    daye "이건 어떻게 될것 같니?"
    dasuk "...계속 커지기만 하는거잖아?"
    chime "그렇지. 이렇게 특정한 값에 한없이 가까워지지 않는 것을 두고 통틀어서 '발산'한다고 해"
    hide eq
    daye "흐음... 이건 어때?"
    show expression "chapter-1-2-0-eq-5.png" as eq at truecenter
    dasuk "흐음...완전히 저세상 가는 것은 아니군"
    chime "(빤히)"
    daye "(뚫어져라..)"
    "....이것은 수렴일까?"
menu:
    "수렴한다":
        jump chapter_1_2_intro_sub_1
    
    "발산한다":
        jump chapter_1_2_intro_sub_2
    
label chapter_1_2_intro_sub_1:
    dasuk "수렴하는것 같은데?"
    daye "...하아"
    chime "...어디에 수렴하는것 같은데?"
    "우선 이 수열은 1 혹은 -1이다"
    "만약 둘 중 어느 한 값에 한없이 가까워진다면 그것이 수렴값이다"
    "...어래?"
    dasuk "미안.. 발산이네"
    daye "...발산이 맞지. 다만 이 경우는 왔다갔다 한다는 의미에서 진동한다고 하기도 해"
    chime "발산의 특별한 경우라서 그런것 같아"
    jump chapter_1_2_1

label chapter_1_2_intro_sub_2:
    dasuk "발산이네"
    daye "정답"
    chime "발산의 특별한 케이스야. '진동'이라고 하기도 해"
    dasuk "특정한 값에 가까워 지지 않는다...에서 발산이네"
    daye "그렇지!"
    "왠지 안심한 표정의 다예"
    dasuk "...어째 안심한 것 같다?"
    daye "이 문제를 보고 발산이 아니다라고 말하는 경우가 있어"
    chime "그런 의미에서 안심했다고나 할가..."
    jump chapter_1_2_1
    
label chapter_1_2_1:
    dasuk "그래서, 수렴과 발산, 그리고 발산의 특별한 경우인 진동이 뭔지는 이해를 했는데"
    chime "...너 문제랑 답 외워서 시험 쳤잖아"
    call dev_select_call
    daye "...교과서와 참고교재 위주의 출제가 좋다면 좋고 싫다면 싫은 부분이 여기 있네"
    "다예가 불만스러운 표정을 짓고 있다"
    chime "다예야?"
    daye "..아무것도 아니야"
    "아무리 봐도 기분이 상한 것 같은데, 왜 저럴까..."
    "흐음...?"
    chime "그럼 조금 난이도를 올려 볼까?"
    show expression "chapter-1-2-1-eq-1.png" as eq at truecenter
    dasuk "흐음?"
    "골때리게 생겼는데..."
    dasuk "일단 나눠 봐야겠어"
    hide eq
    show chime default
    "분모분자에 0이 아닌 수를 곱해도 극한값은 변하지 않을 것이다"
    dasuk "식을 이렇게 바꿔볼께!"
    "n은 임의의 자연수이니까 아무 문제없겠지"

label chapter_1_2_1_Example:
    show expression "chapter-1-2-1-eq-2.png" as eq at truecenter
    "n으로 나누기를 두 번 해본 결과, 식은 이렇게 바뀌었는데"
    "답은 뭘까?"
    hide eq
    menu:
        "1. 발산한다":
            call chapter_1_2_1_sub_False
        "2. 0":
            call chapter_1_2_1_sub_False
        "3. 1/4":
            call chapter_1_2_1_sub_True
        "4. 1":
            call chapter_1_2_1_sub_False
    #정답이 나오지 않으면 빠져나올 수 없는 구조
    "어우 겨우 맞췄네"
    dasuk "그럼 이제 수열의 극한은 끝난거야?"
    show chime default at center:
        xalign 0.7
    show daye default at center:
        xalign 0.3
    chime "....."
    daye "...이제 연습을 해야지?"
    hide chime
    hide daye
    "으아아아아악!!"
    jump chapter_1_2_2_Ex1

label chapter_1_2_1_sub_True:
    chime "정답!"
    return
    
label chapter_1_2_1_sub_False:
    chime "....아니야"
    "다시 생각해 볼까?
    jump chapter_1_2_1_Example

label chapter_1_2_2_ExFailBadEndingWarning:
    daye "....머리가 정말 안돌아가는건가..."
    chime "글쎄다..."
    dasuk "...그냥 외울까?"
    "....Bad Ending?"
    return

label chapter_1_2_2_Ex1: #다양한 종류의 수열의 극한
    "개발자" "그래서 예제풀이를 어떻게 구현해야 할까"
    call dev_select_call
    show daye default
    daye "그러면 이것을 한 번 봐줄래?"
    hide daye
    dasuk "어디보자..."
    show expression "chapter-1-2-2-eq-1.png" as eq at truecenter
    #예제
    dasuk "이건...."
    "역시 이것도 조금 깔끔하게 만들 필요가 있겠어"
    hide eq
    "그럼 일단 이걸 이렇게 하고..."
    show expression "chapter-1-2-2-eq-2.png"as eq at truecenter
    #풀이
    dasuk "어디보자...이거 일단"
    "식을 조작하는 작업은 끝냈는데...일단 수렴/발산 여부부터 말해보자"
    hide eq
    menu:
        "수렴하네":
            daye "응, 수렴해"
        "발산하네":
            chime "아니, 수렴하는데"
	daye "...1/n 극한에 상수만 붙인 거잖아"
	dasuk "....."
	daye "뭘 그렇게 생각할것까지야...."
	dasuk "...."
	menu:
		"극한값은 0이다.":
			"개발자" "정답 루틴"
		"다예의 말에 발끈한다":
			"개발자" "다예-호감도감소-이벤트 구성"
		"상수배 했지만 1/n의 극한값이 0이라서 0*(3/4)=0이다냥!!!":
			"개발자" "뭐 어떻게 처리해볼까"
    jump chapter_1_2_2_Ex2:

label chapter_1_2_2_Ex2:
    call dev_select_call
    show daye default
    daye "...그럼 다음문제 간다."
    "다예가 칠판에 문제를 쓰고 있다."
    if high_edu > 0:
        dasuk "나도 저렇게 수학을 잘 할수 있다면..."
        daye "...응?"
        dasuk "아..아무것도 아닙니다."
        daye "....그래"
    hide daye
    "....."
    "........."
    daye "자, 쉬운 문제니까 한 번 풀어봐"
    show expression "chapter-1-2-2-eq-3.png" as eq at truecenter
    dasuk "흐음...."
    hide eq
    menu:
        "n으로 나눠본다.":
            "풀이"
            call chapter_1_2_2_Ex2_solve
        "발산":
            "정답"
            call chapter_1_2_2_Ex2_solve
        "수렴":
            chime "오답"
            daye "하아..."
            "개발자" "....이건 좀 심한데"
            daye "있잖아..."
            chime "너 어디 아파?"
            dasuk "으음..."
            "수렴과 발산을 착각했나?"
            "손이 미끄러진건가 말실수를 한 건가"
            "뭔가 "
            daye "...집에가자..."
            "배드엔딩. 미적분포기자"
            

label chapter_1_2_2_Ex2_solve:
    call dev_select_call
    "식을 우선 알아보기 쉽게 정리해주자."
    show expression "chapter-1-2-2-eq-4.png" as eq at truecenter
    dasuk "이렇게 나눠주고...."
    chime "흐음... 정석적인 풀이네"
    daye "그렇지. 굉장히 정석적이야."
    hide eq
    jump chapter_1_2_2_Ex3

label chapter_1_2_2_Ex3:
    call dev_select_call
    show chime default
    chime "그럼 이번문제는.."
    #power-limit
    hide chime
    show expression "chapter-1-2-2-eq-5.png" as eq at truecenter
    dasuk "흐음....일단 증감을 생각해볼까"
    hide eq
    "1/n처럼 감소하며, 0 이상의 값을 가지는 수열이다."
    "굉장히 빠르게 감소하는 수열이긴 한데 결국은 0 가까이 간다."
    show expression "chapter-1-2-2-eq-6.png" as eq at treucenter
    dasuk "0"
    hide eq
    show daye default:
        xalign 0.3
    daye "흐음..."
    hide daye
    show cime default:
        xalign 0.7:
    chime "너무 쉬웠나?"
    hide chime
    show daye default:
        xalign 0.3
    daye "지수의 극한을 이해한것으로 굉장한 성과라고 생각하는데"
    show expression "chapter-1-2-2-eq-7.png" as eq at truecenter
    daye "이건 어때?"
    hide eq
    menu:
        "수렴":
            "오답 루틴"
        "발산":
            "정답 루틴"
    jump chapter_1_2_2_Ex4

label chapter_1_2_2_Ex4:
    call dev_select_call
    chime "난이도를 올려볼까?"
    daye "굳이 해야하나..?"
    chime "...처음부터 하는 거니까"
    dasuk "암기로 때워서 미안!!"
    menu:
        "차임이에게 예제를 요청한다":
            show chime default
            chime "....?"
            hide chime
            call chapter_1_2_2_Ex4_chime
            "개발자" "어떻게 해야 잘 부탁할 수 있을까"
            "냥발자" "그러게 말입니다"
            "움프" "그러게"
        "다예에게 예제를 요청한다":
            show daye default
            daye "....?"
            hide daye
            call chapter_1_2_2_Ex4_daye
            "개발자" "일단 분기를 만들어 놨는데"
            "냥발자" "에라이"
    "이다음 어쩌냥"
    return

label chapter_1_2_2_Ex4_chime:
    call dev_select_call
    show chime default
    chime "흐음..?"
    dasuk "....부탁할께"
    chime "...어디보자. 괜찮은 예제가 있을텐데"
    "차임이가 개*리를 뒤적거리고 있다"
    "개발자" "개소리를 뒤적거리고 있다고?"
    daye "시끄러. 별 하나 빼먹은 놈아"
    hide chime
    "차임이가 문제를 적고 있다.."
    chime "...."
    chime "........."
    chime "다 적었어!"
    dasuk "흐음..?"
    show expression "chapter-1-2-2-eq-Ex4-1.png" as eq at truecenter
    dasuk "어디보자..."
    "우선 저기 2와 5의 거듭제곱에 관한 항은 0으로 가는 것을 이미 알고 있다."
    dasuk "우선 하나를 지워봐야 겠어"
    hide eq
    chime "(반짝반짝)"
    daye "(빤히)"
    dasuk "....."
    show expression "chapter-1-2-2-eq-Ex4-chime-2.png" as eq at truecenter
    dasuk "이렇게 2의 n거듭제곱을 분모분자에 곱해주자."
    chime "응응!"
    dasuk "그러면 이 식은 어떻게 되냐하면..."
    call spoiler_warning
    hide eq
    show expression "chapter-1-2-2-eq-Ex4-chime-3.png" as eq at truecenter
    dasuk "이렇게 된단 말이지..."
    hide eq
    "자, 그럼 이 계산을 어떻게 마무리 할까?"
    menu:
        "2/5의 n거듭제곱은 0이니까...":
            "2/5의 n거듭제곱에 0을 대입한다."
        "2/5의 n거듭제곱항은 무시할 수 있으니까...":
            "그 항을 지운 형태로 식을 변형한다"
    #사실 똑같은 소리라서
    show expression "chapter-1-2-2-eq-Ex4-Ans.png" as eq at truecenter
    chime "좋아!"
    dasuk "오예스!!"
    hide eq
    "개발자" "...먹고싶다"
    
    "이후 다예가 5의 n거듭제곱을 곱하여 풀 수 있다는 말을 하는데..."
    "개발자" "다른 풀이를 보기 위해 만들어둔 서브스토리 입니다."
    "개발자" "다른 풀이를 보고 싶으면 '본다'를 선택"
    "개발자" "그냥 넘어가고 싶으면 '보지 않는다'를 선택"
    "개발자" "이후 중등교육(미적분I/미적분II)/고등교육(다변수/벡터/미분방정식) 등 분기에는 영향이 없습니다."
    "개발자" "'다른 풀이'를 보시겠습니까?' 메시지가 출력될 경우 참고해주세요!"
    "다른 풀이 안내" "다른 풀이를 보시겠습니까?"
    menu:
        "본다":
            jump label chapter_1_2_2_Ex4_daye
        "보지 않는다":
            "파구현"
        "몰라":
            "솔구현"

    return

label chapter_1_2_2_Ex4_daye:
    call dev_select_call
    show daye default
    "나는 다예를 바라보았다."
    daye "왜"
    hide daye
    dasuk "다예언니!! 예제 주세요!!"
    daye "...예제가 없어서 맛이 갔나?"
    dasuk "아무래도 그런것 같은데"
    chime "시나리오 라이터가 콜라마시고 쓴것 같은데"
    "개발자" "ㄲㅡ어억 다예언니이"
    daye "예제 줄께 조금만 기다려"
    show daye default
    "...."
    "다예가 칠판에 식을 쓰고 있다."
    dasuk "l"
    dasuk "li"
    dasuk "lim"
    dasuk "......"
    "아"
    "다예가 스르륵 하고 극한 기호를 쓰고 있다."
    #"너무 매력적이야"
    #금사빠냐 씨부레
    #니가썻잖아 움프시키야
    daye "자..완료!"
    hide daye
    dasuk "흐음...."
    show expression "chapter-1-2-2-eq-Ex4-1.png" as eq at treucenter
    daye "자.. 풀어보렴!"
    dasuk "흐음...저 5가 거슬린다, 이 말입니다."
    "5의 n승을 분모분자에 곱해 보자"
    "....."
    hide eq
    "....."
    show expression "chapter-1-2-2-eq-Ex4-daye-2.png"
    dasuk "이렇게 변형된다..."
    "자 그럼 이제 이것을 어떻게 끝장을 볼까?"
    hide eq
    menu:
        "상수항을 무시해본다":
            "5/2의 n거듭제곱은 무한대로 간다. 즉, 상수항은 무시해도 무방하겠지"
            "마음속으로 상수항을 지운다.."
        "양변을 5/2의 n제곱으로 나눈다고 생각해본다":
            "무한대 항이 있으니까, 가장 기초적인 방법이라고나 할까"
            "그러면 상수항에 곱해진 2/5의 n거듭제곱은 0으로 가게 된다."
            "그러면 결국 0이군"
    dasuk "답은...
    show expression "chapter-1-2-2-eq-Ex4-daye-3.png" as eq at truecenter
    dasuk "...이와 같습니다."
    daye "오케이!"
    "차임이가 2의 n거듭제곱을 곱하여도 할 수 있다고 한다."
    "개발자" "다른 풀이를 보기 위해 만들어둔 서브스토리 입니다."
    "개발자" "다른 풀이를 보고 싶으면 '본다'를 선택"
    "개발자" "그냥 넘어가고 싶으면 '보지 않는다'를 선택"
    "개발자" "이후 중등교육(미적분I/미적분II)/고등교육(다변수/벡터/미분방정식) 등 분기에는 영향이 없습니다."
    "개발자" "'다른 풀이'를 보시겠습니까?' 메시지가 출력될 경우 참고해주세요!"
    "다른 풀이 안내" "다른 풀이를 보시겠습니까?"
    menu:
        "본다":
            jump chapter_1_2_2_Ex4_chime
        "보지 않는다":
            "개발자" "미구현"
    return

label spoiler_warning:
    "개발자" "다음으로 넘어가기 전에 여러분도 풀어보시기 바랍니다!"
    "개발자" "스포일러 주의(5 중 1)"
    "개발자" "스포일러 주의(5 중 2)"
    "개발자" "스포일러 주의(5 중 3)"
    "개발자" "스포일러 주의(5 중 4)"
    "개발자" "스포일러 주의(5 중 5)"
    return

label dev_select_call:
    "개발자를 위하여 dev_selection 블록을 만들었습니다. 원하는 챕터로 점프할 수 있습니다."
    menu:
        "call dev_selection":
            call dev_selection
        "jump dev_selection":
            jump dev_selection
        "그냥 진행하기":
            "즐거운 디버깅 합시다."
    return

label dev_selection:
    menu:
        "start : 프롤로그":
            jump start
        "chapter_1 : 극한":
            menu:
                "chapter_1_1 : 극한의 정의와 설명":
                    jump chapter_1_1_intro
                "chapter_1_2 : 수열의 극한의 수렴과 발산":
                    menu:
                        "chapter_1_2_intro : 수열의 극한의 설명":
                            jump chapter_1_2_intro
                        "chapter_1_2_1 : 기초적인 수열의 극한":
                            jump chapter_1_2_1
                        "chapter_1_2_2 : 다양한 수열의 극한":
                            menu:
                                "chapter_1_2_2 의 시작":
                                    jump chapter_1_2_2
                                "chpater_1_2_2 예제1":
                                    jump chapter_1_2_2_Ex1
                                "chpater_1_2_2 예제2":
                                    jump chapter_1_2_2_Ex2
                                "chapter_1_2_2 예제3":
                                    jump chapter_1_2_2_Ex3
                                "chapter_1_2_2 예제4":
                                    jump chapter_1_2_2_Ex4
    return