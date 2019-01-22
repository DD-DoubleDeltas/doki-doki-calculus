# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")
define daye = Character('박다예',color="#ffffff")
define dasuk = Character('민다석',color="#ffffff")
define chime = Character('이차임',color="#ffffff")
# 여기에서부터 게임이 시작합니다.

label start:
    #장면 : 교실
    "딩동댕동"
    dasuk "으아아 드디어 시험이 끝났다"
    chime "드디어 끝이네!"
    chime "시험은 잘 봤니?"
    dasuk "나 국어 망해가지고..."
    "이차임. 인미고등학교 2학년"
    "나와 같은반인, 소꿉친구다"
    "뭐, 이렇게 시험 끝나고 이런저런 이야기를 나누는게 이상한건 아니라고"
    chime "수학은 잘 봤냐?"
    dasuk "가채점 결과 87점"
    chime "생각보다는 잘 나왔는걸? 진짜야"?
    dasuk "나 수학 원래 잘 하는데?"
    chime "같이 숙제할 때 봤는데, 너 외워서 하는것 같던데"
    dasuk "메모리에 올려두고 연산을 줄이는 것도 꽤나 좋은 기법이란다"
    chime "너정도 머리되는 애면 연산도 꽤나 잘 할것 같단 말이야"
    "아..차임아 제발"
    "이럴때는..!"
    dasuk "흠.. 나는 일단 집에 갈거야"
    "return 0; //이곳을 탈출한다"
    #TIP추가. 다석 : 프로그래밍
    chime "어디가..!"
    
    #장면 : 하교길
    "집에 가는 길은 정말 애매하다."
    "버스를 타기에는 너무 가깝다."
    dasuk "몇 정거장 갈 바에야..."
    "택시는 안잡힌다"
    dasuk "콜택시 부르기는 귀찮고, 돈도 아깝고"
    "그럼 걸어야지."
    dasuk "전혀 애매하지 않군"
    "그런 생각을 하며 오늘도 집으로 간다"
    dasuk "흠.. 오늘도 같은 길을 가는 것인가?"
    "항상 같은 길을 가는 학생이 있다"
    "흑발에 긴 머리."
    "어떤 날은 내가 앞서가고, 어떤 날은 그녀가 앞서 간다."
    "오늘은 그녀가 앞서 간다"
    dasuk "흠.."
    "나는 거의 등속력으로 움직인다."
    "길을 x축과 같이 두면 dx/dt = Constant(상수)"
    dasuk "이걸 기억하고 있군"
    "나는 보통 시험을 치면 바로 포맷된다"
    "그런데 이것을 기억하고 있구나."
    "굉장히 의아하다는 생각을 하며 나는 계속 걸어갔고"
    "그녀의 머리(H) 나의 눈(O) 그녀의 발(F)"
    "각 HOF가 증가하고 있다는 것을 나는 인지하지 못했다."
    "HOF가 거의 3.14"에 다다랐을 무렵 나는 그녀와 충돌하였다"
    dasuk "아, 미안!"
    "???" "......민다석"
    dasuk "....아... 박다예?"
    "출석번호상 바로 나 다음인데, 이름 정도는 알고 있다"
    "수학과 과학에 있어서는 상위권을 놓치지 않는 그녀"
    "국어나 영어는... 글쎄?"
    daye "이제 알았냐?"
    dasuk "히익"
    "얘 무서워"
    daye "각 Head-Eye-Foot이 pi에 근접하는 것을 알았으면 멈춰야 할 거 아냐?!"
    dasuk "....미안"
    daye "흐음... 마침 잘 된것 같다"
    "응??? 갑자기 훅 들어오네?"
    "우리 반에서 그렇게 말 많이하고 지낸 그런사이 아닌데"
    daye "자율동아리를 만들꺼야. 들어와라"
    dasuk "........."
    "아...귀찮은데"
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
    jump chapter_1_1
 
 
 #챕터1, 극한
 label chapter_1_1_intro:
    dasuk "...그래서 일단 책을 들고 왔어"
    chime "다석이가 시험기간이 아닐 때 책을 들고 있네"
    dasuk "외울 때가 아니면 책을 볼 필요가 딱히 없으니까"
    daye "찌릿"
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
    show expression "chapter-1-1-pic-1.png" as pic
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
	show expression "chapter-1-1-eq-1.png" as eq
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
	chime "너가 방금 말한 h를 0으로 접근시킨 평균변화율은 나중에 순간변화율이라 다시 나오겠지만"
	chime "식으로 쓰면 이렇게...."
	show expression "chapter-1-1-eq-2.png" as eq
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
	$ hischool += 1
	dasuk "저기 lim기호 보고 생각난건데"
	show expression "chapter-1-1-eq-3.png" as eq
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
	
label chapter_1_2_intro:
	dasuk "수열의 극한이라..."
	daye "수열에 대해서 기억하니?"
	chime "과연?"
	dasuk "수의 나열"
	chime "딱히 틀린말은 아닌것 같은데"
	daye "...고등학교에서 수열의 정의를 어떻게 하고 있는지는 모르겠지만, 자연수집합에서 실수집합으로 가는 함수라고 보렴..."
	
	
	
	
	
    
    
    
    
    
    
    
    
    

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"
    daye "그렇다냥"

    return
