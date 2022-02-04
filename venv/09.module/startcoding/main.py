# 1. import 패키지.모듈
# import unit.character as uc
# import unit.item as ui
# import unit.monster as um
#
# uc.test()
#
# #2. from 패키지 import 모듈
# from unit import item
# item.test()

#3. from 패키지 import *
# * 를 쓰려면 __init__ 모듈 수정이 필요
# from unit import *
#
# character.test()
# item.test()
# monster.test()

#4 . import 패키지
import unit

unit.monster.test()
unit.item.test()
unit.item.test()