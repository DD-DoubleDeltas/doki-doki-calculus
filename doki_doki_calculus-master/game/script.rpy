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
    #색깔 입혀서 컬러 표시하는 방법이 있다면 예제를 부탁합니다!
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
    

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"
    daye "그렇다냥"

    return
