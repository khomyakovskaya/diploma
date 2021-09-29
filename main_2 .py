# -*- coding: utf-8 -*-
import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui

from старт import Ui_StartWindow
from главнаяI import Ui_GlavnayaIWindow
from главнаяII import Ui_GlavnayaIIWindow
from главнаяIII import Ui_GlavnayaIIIWindow
from оглавление import Ui_OglavlenieWindow
from теория_1 import Ui_Teoria1Window
from теория_2 import Ui_Teoria2Window
from теория_3 import Ui_Teoria3Window
from теория_4 import Ui_Teoria4Window
from теория_5 import Ui_Teoria5Window
from теория_6 import Ui_Teoria6Window
from теория_7 import Ui_Teoria7Window
from теория_8 import Ui_Teoria8Window
from теория_9 import Ui_Teoria9Window
from теория_10 import Ui_Teoria10Window
from теория_11 import Ui_Teoria11Window
from теория_12 import Ui_Teoria12Window
from теория_13 import Ui_Teoria13Window
from теория_14 import Ui_Teoria14Window
from теория_15 import Ui_Teoria15Window
from теория_16 import Ui_Teoria16Window
from теория_17 import Ui_Teoria17Window
from теория_18 import Ui_Teoria18Window
from теория_19 import Ui_Teoria19Window
from теория_20 import Ui_Teoria20Window
from теория_21 import Ui_Teoria21Window
from теория_22 import Ui_Teoria22Window
from теория_23 import Ui_Teoria23Window
from теория_24 import Ui_Teoria24Window
from теория_25 import Ui_Teoria25Window
from теория_26 import Ui_Teoria26Window
from теория_27 import Ui_Teoria27Window
from теория_28 import Ui_Teoria28Window
from теория_29 import Ui_Teoria29Window
from теория_30 import Ui_Teoria30Window
from теория_31 import Ui_Teoria31Window
from теория_32 import Ui_Teoria32Window
from теория_33 import Ui_Teoria33Window
from теория_34 import Ui_Teoria34Window
from теория_35 import Ui_Teoria35Window
from теория_36 import Ui_Teoria36Window
from теория_37 import Ui_Teoria37Window
from теория_38 import Ui_Teoria38Window
from теория_39 import Ui_Teoria39Window
from тестprompt0I import Ui_TestPrompt0IWindow
from тестprompt0II import Ui_TestPrompt0IIWindow
from тестprompt0III import Ui_TestPrompt0IIIWindow
from тестprompt import Ui_TestPromptWindow
from тест0 import Ui_Test0Window
from тест import Ui_TestWindow
from результат import Ui_ResultatWindow
from вопросыI import Ui_QuestionsIWindow
from вопросыII import Ui_QuestionsIIWindow
from вопросыIII import Ui_QuestionsIIIWindow
from верно import Ui_Right
from неверно import Ui_Wrong
from результатprom import Ui_ResultatPromWindow
#"ОБУЧЕНИЕ И КОНТРОЛЬ" КАТЕГОРИИ I
#номер вопроса "Обучение и контроль" категории I
numberprompt_one = 0
#расположение вопроса в списке "Обучение и контроль" категории I
addressprompt_one = 0
#количество набранных баллов "Обучение и контроль" категории I
resultprompt_one = 0
#КОНТРОЛЬНЫЙ ТЕСТ КАТЕГОРИИ I
#номер вопроса контрольного теста категории I
number_one = 0
#количество набранных баллов контрольного теста категории I
result_one =0
#"ОБУЧЕНИЕ И КОНТРОЛЬ" КАТЕГОРИИ II
#номер вопроса "Обучение и контроль" категории II
numberprompt_two = 0
#расположение вопроса в списке "Обучение и контроль" категории II
addressprompt_two = 0
#количество набранных баллов "Обучение и контроль" категории II
resultprompt_two = 0
#КОНТРОЛЬНЫЙ ТЕСТ КАТЕГОРИИ II
#номер вопроса контрольного теста категории II
number_two = 0
#количество набранных баллов контрольного теста категории II
result_two = 0
#"ОБУЧЕНИЕ И КОНТРОЛЬ" КАТЕГОРИИ III
#номер вопроса "Обучение и контроль" категории III
numberprompt_three = 0
#расположение вопроса в списке "Обучение и контроль" категории III
addressprompt_three = 0
#количество набранных баллов "Обучение и контроль" категории III
resultprompt_three = 0
#КОНТРОЛЬНЫЙ ТЕСТ КАТЕГОРИИ III
#номер вопроса контрольного теста категории III
number_three = 0
#количество набранных баллов контрольного теста категории III
result_three = 0


#начальный экран
class Start(QtWidgets.QMainWindow,Ui_StartWindow):
    def __init__(self):
        super(Start, self).__init__()
        self.setupUi(self)

        self.btn_I.clicked.connect(self.onGlavnayaI)
        self.btn_II.clicked.connect(self.onGlavnayaII)
        self.btn_III.clicked.connect(self.onGlavnayaIII)
#переход к главному экрану категории I
    def onGlavnayaI(self):
        self.GlavnayaI = Glavnaya_I()
        self.GlavnayaI.show()
        self.hide()

# переход к главному экрану категории II
    def onGlavnayaII(self):
        self.GlavnayaII = Glavnaya_II()
        self.GlavnayaII.show()
        self.hide()

#переход к главному экрану категории III
    def onGlavnayaIII(self):
        self.GlavnayaIII = Glavnaya_III()
        self.GlavnayaIII.show()
        self.hide()

#главный экран категории I
class Glavnaya_I(QtWidgets.QMainWindow,Ui_GlavnayaIWindow):
    def __init__(self):
        super(Glavnaya_I, self).__init__()
        self.setupUi(self)

        self.btn_teoriya.clicked.connect(self.onTeoriaOneI)
        self.btn_test_podskazka.clicked.connect(self.onTestPrompt0I)
        self.btn_contr_test.clicked.connect(self.onTest0I)
        self.btn_user.clicked.connect(self.changeUser)

#переход к режиму обучения "Теория" для категории I
    def onTeoriaOneI(self):
        self.teoria_one = TeoriaOne()
        self.teoria_one.show()
        self.hide()

# переход к режиму обучения "Обучение и контроль" для категории I
    def onTestPrompt0I(self):
        self.testprompt_0 = TestPrompt_0I()
        self.testprompt_0.show()
        self.hide()

# переход к режиму обучения "Контрольный тест" для категории I
    def onTest0I(self):
        self.test_0 = Test_0I()
        self.test_0.show()
        self.hide()

#переход на экран "Старт"
    def changeUser(self):
        self.change_user = Start()
        self.change_user.show()
        self.close()
#главный экран категории II
class Glavnaya_II(QtWidgets.QMainWindow,Ui_GlavnayaIIWindow):
    def __init__(self):
        super(Glavnaya_II, self).__init__()
        self.setupUi(self)

        self.btn_teoriya.clicked.connect(self.onTeoriaOneII)
        self.btn_test_podskazka.clicked.connect(self.onTestPrompt0II)
        self.btn_contr_test.clicked.connect(self.onTest0II)
        self.btn_user.clicked.connect(self.changeUser)

    def onTeoriaOneII(self):
        self.teoria_oneII = TeoriaOneII()
        self.teoria_oneII.show()
        self.hide()

    def onTestPrompt0II(self):
        self.testprompt_0II = TestPrompt_0II()
        self.testprompt_0II.show()
        self.hide()

    # переход к режиму обучения "Контрольный тест" для категории II
    def onTest0II(self):
        self.test_0II = Test_0II()
        self.test_0II.show()
        self.hide()

    # переход на экран "Старт"
    def changeUser(self):
        self.change_user = Start()
        self.change_user.show()
        self.close()

#главный экран категории III
class Glavnaya_III(QtWidgets.QMainWindow,Ui_GlavnayaIIIWindow):
    def __init__(self):
        super(Glavnaya_III, self).__init__()
        self.setupUi(self)

        self.btn_teoriya.clicked.connect(self.onTeoriaOneIII)
        self.btn_test_podskazka.clicked.connect(self.onTestPrompt0III)
        self.btn_contr_test.clicked.connect(self.onTest0III)
        self.btn_user.clicked.connect(self.changeUser)

    def onTeoriaOneIII(self):
        self.teoria_oneIII = TeoriaOneIII()
        self.teoria_oneIII.show()
        self.hide()

    def onTestPrompt0III(self):
        self.testprompt_0III = TestPrompt_0III()
        self.testprompt_0III.show()
        self.hide()

    # переход к режиму обучения "Контрольный тест" для категории III
    def onTest0III(self):
        self.test_0III = Test_0III()
        self.test_0III.show()
        self.hide()

    # переход на экран "Старт"
    def changeUser(self):
        self.change_user = Start()
        self.change_user.show()
        self.close()

#теория 1 категории I
class TeoriaOne(QtWidgets.QMainWindow,Ui_Teoria1Window):
    def __init__(self):
        super(TeoriaOne, self).__init__()
        self.setupUi(self)

        self.btn_dalee1.clicked.connect(self.onTeoriaTwo)
        self.btn_oglavlenie1.clicked.connect(self.oglavlenieI)
        self.btn_glavnaya1.clicked.connect(self.returnGlavnayaI)

#переход к экрану 'теория 2' категории I
    def onTeoriaTwo(self):
        self.teoria_two = TeoriaTwo()
        self.teoria_two.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieI(self):
        self.oglavlenie_1 = Oglavlenie()
        self.oglavlenie_1.show()

# переход к главному экрану 'теория 2' категории I
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

#экран 'теория 2' категории I
class TeoriaTwo(QtWidgets.QMainWindow,Ui_Teoria2Window):
    def __init__(self):
        super(TeoriaTwo, self).__init__()
        self.setupUi(self)

        self.btn_dalee2.clicked.connect(self.onTeoriaThree)
        self.btn_glavnaya2.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie2.clicked.connect(self.oglavlenie)
        self.btn_return2.clicked.connect(self.returnTeoriaOne)

#переход к экрану 'теория 3' категории I
    def onTeoriaThree(self):
        self.teoria_three = TeoriaThree()
        self.teoria_three.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

#переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к главному экрану 'теория 1' категории I
    def returnTeoriaOne(self):
        self.T1I = TeoriaOne()
        self.T1I.show()
        self.hide()

#экран 'теория 3' категории I
class TeoriaThree(QtWidgets.QMainWindow,Ui_Teoria3Window):
    def __init__(self):
        super(TeoriaThree, self).__init__()
        self.setupUi(self)

        self.btn_dalee3.clicked.connect(self.onTeoriaFour)
        self.btn_glavnaya3.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie3.clicked.connect(self.oglavlenie)
        self.btn_return3.clicked.connect(self.returnTeoriaTwo)

#переход к экрану 'теория 4'
    def onTeoriaFour(self):
        self.teoria_four = TeoriaFour()
        self.teoria_four.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 2' категории I
    def returnTeoriaTwo(self):
        self.T2I = TeoriaTwo()
        self.T2I.show()
        self.hide()

#экран 'теория 4' категории I
class TeoriaFour(QtWidgets.QMainWindow,Ui_Teoria4Window):
    def __init__(self):
        super(TeoriaFour, self).__init__()
        self.setupUi(self)

        self.btn_dalee4.clicked.connect(self.onTeoriaFive)
        self.btn_glavnaya4.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie4.clicked.connect(self.oglavlenie)
        self.btn_return4.clicked.connect(self.returnTeoriaThree)

# переход к экрану 'теория 5'
    def onTeoriaFive(self):
        self.teoria_five = TeoriaFive()
        self.teoria_five.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

#переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 3' категории I
    def returnTeoriaThree(self):
        self.T3I = TeoriaThree()
        self.T3I.show()
        self.hide()

#экран 'теория 5' категории I
class TeoriaFive(QtWidgets.QMainWindow,Ui_Teoria5Window):
    def __init__(self):
        super(TeoriaFive, self).__init__()
        self.setupUi(self)

        self.btn_dalee5.clicked.connect(self.onTeoriaSix)
        self.btn_glavnaya5.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie5.clicked.connect(self.oglavlenie)
        self.btn_return5.clicked.connect(self.returnTeoriaFour)

#переход к экрану 'теория 6'
    def onTeoriaSix(self):
        self.teoria_six = TeoriaSix()
        self.teoria_six.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

#переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 4' категории I
    def returnTeoriaFour(self):
        self.T4I = TeoriaFour()
        self.T4I.show()
        self.hide()

#экран 'теория 6' категории I
class TeoriaSix(QtWidgets.QMainWindow,Ui_Teoria6Window):
    def __init__(self):
        super(TeoriaSix, self).__init__()
        self.setupUi(self)

        self.btn_dalee6.clicked.connect(self.onTeoriaSeven)
        self.btn_glavnaya6.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie6.clicked.connect(self.oglavlenie)
        self.btn_return6.clicked.connect(self.returnTeoriaFive)

# переход к экрану 'теория 7'
    def onTeoriaSeven(self):
        self.teoria_seven = TeoriaSeven()
        self.teoria_seven.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 5' категории I
    def returnTeoriaFive(self):
        self.T5I = TeoriaFive()
        self.T5I.show()
        self.hide()

#экран 'теория 7' категории I
class TeoriaSeven(QtWidgets.QMainWindow,Ui_Teoria7Window):
    def __init__(self):
        super(TeoriaSeven, self).__init__()
        self.setupUi(self)

        self.btn_dalee7.clicked.connect(self.onTeoriaEight)
        self.btn_glavnaya7.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie7.clicked.connect(self.oglavlenie)
        self.btn_return7.clicked.connect(self.returnTeoriaSix)

# переход к экрану 'теория 8'
    def onTeoriaEight(self):
        self.teoria_eight = TeoriaEight()
        self.teoria_eight.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 6' категории I
    def returnTeoriaSix(self):
        self.T6I = TeoriaSix()
        self.T6I.show()
        self.hide()

#экран 'теория 8' категории I
class TeoriaEight(QtWidgets.QMainWindow,Ui_Teoria8Window):
    def __init__(self):
        super(TeoriaEight, self).__init__()
        self.setupUi(self)

        self.btn_dalee8.clicked.connect(self.onTeoriaNine)
        self.btn_glavnaya8.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie8.clicked.connect(self.oglavlenie)
        self.btn_return8.clicked.connect(self.returnTeoriaSeven)

# переход к экрану 'теория 9'
    def onTeoriaNine(self):
        self.teoria_nine = TeoriaNine()
        self.teoria_nine.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 7' категории I
    def returnTeoriaSeven(self):
        self.T7I = TeoriaSeven()
        self.T7I.show()
        self.hide()

#экран 'теория 9' категории I
class TeoriaNine(QtWidgets.QMainWindow,Ui_Teoria9Window):
    def __init__(self):
        super(TeoriaNine, self).__init__()
        self.setupUi(self)

        self.btn_dalee9.clicked.connect(self.onTeoriaTen)
        self.btn_glavnaya9.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie9.clicked.connect(self.oglavlenie)
        self.btn_return9.clicked.connect(self.returnTeoriaEight)

# переход к экрану 'теория 10'
    def onTeoriaTen(self):
        self.teoria_ten = TeoriaTen()
        self.teoria_ten.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 8' категории I
    def returnTeoriaEight(self):
        self.T8I = TeoriaEight()
        self.T8I.show()
        self.hide()

#экран 'теория 10' категории I
class TeoriaTen(QtWidgets.QMainWindow,Ui_Teoria10Window):
    def __init__(self):
        super(TeoriaTen, self).__init__()
        self.setupUi(self)

        self.btn_dalee10.clicked.connect(self.onTeoriaEleven)
        self.btn_glavnaya10.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie10.clicked.connect(self.oglavlenie)
        self.btn_return10.clicked.connect(self.returnTeoriaNine)

# переход к экрану 'теория 11'
    def onTeoriaEleven(self):
        self.teoria_eleven = TeoriaEleven()
        self.teoria_eleven.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 9' категории I
    def returnTeoriaNine(self):
        self.T9I = TeoriaNine()
        self.T9I.show()
        self.hide()

#экран 'теория 11' категории I
class TeoriaEleven(QtWidgets.QMainWindow,Ui_Teoria11Window):
    def __init__(self):
        super(TeoriaEleven, self).__init__()
        self.setupUi(self)

        self.btn_dalee11.clicked.connect(self.onTeoriaTwelve)
        self.btn_glavnaya11.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie11.clicked.connect(self.oglavlenie)
        self.btn_return11.clicked.connect(self.returnTeoriaTen)

# переход к экрану 'теория 12'
    def onTeoriaTwelve(self):
        self.teoria_twelve = TeoriaTwelve()
        self.teoria_twelve.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 10' категории I
    def returnTeoriaTen(self):
        self.T10I = TeoriaTen()
        self.T10I.show()
        self.hide()

#экран 'теория 12' категории I
class TeoriaTwelve(QtWidgets.QMainWindow,Ui_Teoria12Window):
    def __init__(self):
        super(TeoriaTwelve, self).__init__()
        self.setupUi(self)

        self.btn_dalee12.clicked.connect(self.onTeoriaThirteen)
        self.btn_glavnaya12.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie12.clicked.connect(self.oglavlenie)
        self.btn_return12.clicked.connect(self.returnTeoriaEleven)

# переход к экрану 'теория 13'
    def onTeoriaThirteen(self):
        self.teoria_thirteen = TeoriaThirteen()
        self.teoria_thirteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 11' категории I
    def returnTeoriaEleven(self):
        self.T11I = TeoriaEleven()
        self.T11I.show()
        self.hide()

#экран 'теория 13' категории I
class TeoriaThirteen(QtWidgets.QMainWindow,Ui_Teoria13Window):
    def __init__(self):
        super(TeoriaThirteen, self).__init__()
        self.setupUi(self)

        self.btn_dalee13.clicked.connect(self.onTeoriaFourteen)
        self.btn_glavnaya13.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie13.clicked.connect(self.oglavlenie)
        self.btn_return13.clicked.connect(self.returnTeoriaTwelve)

# переход к экрану 'теория 14'
    def onTeoriaFourteen(self):
        self.teoria_fourteen = TeoriaFourteen()
        self.teoria_fourteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 12' категории I
    def returnTeoriaTwelve(self):
        self.T12I = TeoriaTwelve()
        self.T12I.show()
        self.hide()

#экран 'теория 14' категории I
class TeoriaFourteen(QtWidgets.QMainWindow,Ui_Teoria14Window):
    def __init__(self):
        super(TeoriaFourteen, self).__init__()
        self.setupUi(self)

        self.btn_dalee14.clicked.connect(self.onTeoriaFifteen)
        self.btn_glavnaya14.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie14.clicked.connect(self.oglavlenie)
        self.btn_return14.clicked.connect(self.returnTeoriaThirteen)

# переход к экрану 'теория 15'
    def onTeoriaFifteen(self):
        self.teoria_fifteen = TeoriaFifteen()
        self.teoria_fifteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 13' категории I
    def returnTeoriaThirteen(self):
        self.T13I = TeoriaThirteen()
        self.T13I.show()
        self.hide()

#экран 'теория 15' категории I
class TeoriaFifteen(QtWidgets.QMainWindow,Ui_Teoria15Window):
    def __init__(self):
        super(TeoriaFifteen, self).__init__()
        self.setupUi(self)

        self.btn_dalee15.clicked.connect(self.onTeoriaSixteen)
        self.btn_glavnaya15.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie15.clicked.connect(self.oglavlenie)
        self.btn_return15.clicked.connect(self.returnTeoriaFourteen)

# переход к экрану 'теория 16'
    def onTeoriaSixteen(self):
        self.teoria_sixteen = TeoriaSixteen()
        self.teoria_sixteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 14' категории I
    def returnTeoriaFourteen(self):
        self.T14I = TeoriaFourteen()
        self.T14I.show()
        self.hide()

#экран 'теория 16' категории I
class TeoriaSixteen(QtWidgets.QMainWindow,Ui_Teoria16Window):
    def __init__(self):
        super(TeoriaSixteen, self).__init__()
        self.setupUi(self)

        self.btn_dalee16.clicked.connect(self.onTeoriaSeventeen)
        self.btn_glavnaya16.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie16.clicked.connect(self.oglavlenie)
        self.btn_return16.clicked.connect(self.returnTeoriaFifteen)

# переход к экрану 'теория 17'
    def onTeoriaSeventeen(self):
        self.teoria_seventeen = TeoriaSeventeen()
        self.teoria_seventeen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 15' категории I
    def returnTeoriaFifteen(self):
        self.T15I = TeoriaFifteen()
        self.T15I.show()
        self.hide()

#экран 'теория 17' категории I
class TeoriaSeventeen(QtWidgets.QMainWindow,Ui_Teoria17Window):
    def __init__(self):
        super(TeoriaSeventeen, self).__init__()
        self.setupUi(self)

        self.btn_dalee17.clicked.connect(self.onTeoriaEighteen)
        self.btn_glavnaya17.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie17.clicked.connect(self.oglavlenie)
        self.btn_return17.clicked.connect(self.returnTeoriaSixteen)

# переход к экрану 'теория 18'
    def onTeoriaEighteen(self):
        self.teoria_eighteen = TeoriaEighteen()
        self.teoria_eighteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 16' категории I
    def returnTeoriaSixteen(self):
        self.T16I = TeoriaSixteen()
        self.T16I.show()
        self.hide()

#экран 'теория 18' категории I
class TeoriaEighteen(QtWidgets.QMainWindow,Ui_Teoria18Window):
    def __init__(self):
        super(TeoriaEighteen, self).__init__()
        self.setupUi(self)

        self.btn_dalee18.clicked.connect(self.onTeoriaNineteen)
        self.btn_glavnaya18.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie18.clicked.connect(self.oglavlenie)
        self.btn_return18.clicked.connect(self.returnTeoriaSeventeen)

# переход к экрану 'теория 19'
    def onTeoriaNineteen(self):
        self.teoria_nineteen = TeoriaNineteen()
        self.teoria_nineteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 17' категории I
    def returnTeoriaSeventeen(self):
        self.T17I = TeoriaSeventeen()
        self.T17I.show()
        self.hide()

#экран 'теория 19' категории I
class TeoriaNineteen(QtWidgets.QMainWindow,Ui_Teoria19Window):
    def __init__(self):
        super(TeoriaNineteen, self).__init__()
        self.setupUi(self)

        self.btn_dalee19.clicked.connect(self.onTeoriaTwenty)
        self.btn_glavnaya19.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie19.clicked.connect(self.oglavlenie)
        self.btn_return19.clicked.connect(self. returnTeoriaEighteen)

# переход к экрану 'теория 20'
    def onTeoriaTwenty(self):
        self.teoria_twenty = TeoriaTwenty()
        self.teoria_twenty.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 18' категории I
    def returnTeoriaEighteen(self):
        self.T18I = TeoriaEighteen()
        self.T18I.show()
        self.hide()

#экран 'теория 20' категории I
class TeoriaTwenty(QtWidgets.QMainWindow,Ui_Teoria20Window):
    def __init__(self):
        super(TeoriaTwenty, self).__init__()
        self.setupUi(self)

        self.btn_dalee20.clicked.connect(self.onTeoriaTwentyOne)
        self.btn_glavnaya20.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie20.clicked.connect(self.oglavlenie)
        self.btn_return20.clicked.connect(self.returnTeoriaNineteen)

# переход к экрану 'теория 21'
    def onTeoriaTwentyOne(self):
        self.teoria_twenty_one = TeoriaTwentyOne()
        self.teoria_twenty_one.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 19' категории I
    def returnTeoriaNineteen(self):
        self.T19I = TeoriaNineteen()
        self.T19I.show()
        self.hide()

#экран 'теория 21' категории I
class TeoriaTwentyOne(QtWidgets.QMainWindow,Ui_Teoria21Window):
    def __init__(self):
        super(TeoriaTwentyOne, self).__init__()
        self.setupUi(self)

        self.btn_dalee21.clicked.connect(self.onTeoriaTwentyTwo)
        self.btn_glavnaya21.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie21.clicked.connect(self.oglavlenie)
        self.btn_return21.clicked.connect(self.returnTeoriaTwenty)

# переход к экрану 'теория 22'
    def onTeoriaTwentyTwo(self):
        self.teoria_twenty_two = TeoriaTwentyTwo()
        self.teoria_twenty_two.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 20' категории I
    def returnTeoriaTwenty(self):
        self.T20I = TeoriaTwenty()
        self.T20I.show()
        self.hide()

#экран 'теория 22' категории I
class TeoriaTwentyTwo(QtWidgets.QMainWindow,Ui_Teoria22Window):
    def __init__(self):
        super(TeoriaTwentyTwo, self).__init__()
        self.setupUi(self)

        self.btn_dalee22.clicked.connect(self.onTeoriaTwentyThree)
        self.btn_glavnaya22.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie22.clicked.connect(self.oglavlenie)
        self.btn_return22.clicked.connect(self.returnTeoriaTwentyOne)

# переход к экрану 'теория 23'
    def onTeoriaTwentyThree(self):
        self.teoria_twenty_three = TeoriaTwentyThree()
        self.teoria_twenty_three.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 21' категории I
    def returnTeoriaTwentyOne(self):
        self.T21I = TeoriaTwentyOne()
        self.T21I.show()
        self.hide()

#экран 'теория 23' категории I
class TeoriaTwentyThree(QtWidgets.QMainWindow,Ui_Teoria23Window):
    def __init__(self):
        super(TeoriaTwentyThree, self).__init__()
        self.setupUi(self)

        self.btn_dalee23.clicked.connect(self.onTeoriaTwentyFour)
        self.btn_glavnaya23.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie23.clicked.connect(self.oglavlenie)
        self.btn_return23.clicked.connect(self.returnTeoriaTwentyTwo)

# переход к экрану 'теория 24'
    def onTeoriaTwentyFour(self):
        self.teoria_twenty_four = TeoriaTwentyFour()
        self.teoria_twenty_four.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 22' категории I
    def returnTeoriaTwentyTwo(self):
        self.T22I = TeoriaTwentyTwo()
        self.T22I.show()
        self.hide()

#экран 'теория 24' категории I
class TeoriaTwentyFour(QtWidgets.QMainWindow,Ui_Teoria24Window):
    def __init__(self):
        super(TeoriaTwentyFour, self).__init__()
        self.setupUi(self)

        self.btn_dalee24.clicked.connect(self.onTeoriaTwentyFive)
        self.btn_glavnaya24.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie24.clicked.connect(self.oglavlenie)
        self.btn_return24.clicked.connect(self.returnTeoriaTwentyThree)

# переход к экрану 'теория 25'
    def onTeoriaTwentyFive(self):
        self.teoria_twenty_five = TeoriaTwentyFive()
        self.teoria_twenty_five.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 23' категории I
    def returnTeoriaTwentyThree(self):
        self.T23I = TeoriaTwentyThree()
        self.T23I.show()
        self.hide()

#экран 'теория 25' категории I
class TeoriaTwentyFive(QtWidgets.QMainWindow,Ui_Teoria25Window):
    def __init__(self):
        super(TeoriaTwentyFive, self).__init__()
        self.setupUi(self)

        self.btn_dalee25.clicked.connect(self.onTeoriaTwentySix)
        self.btn_glavnaya25.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie25.clicked.connect(self.oglavlenie)
        self.btn_return25.clicked.connect(self.returnTeoriaTwentyFour)

# переход к экрану 'теория 26'
    def onTeoriaTwentySix(self):
        self.teoria_twenty_six = TeoriaTwentySix()
        self.teoria_twenty_six.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'теория 24' категории I
    def returnTeoriaTwentyFour(self):
        self.T24I = TeoriaTwentyFour()
        self.T24I.show()
        self.hide()

#экран 'теория 26' категории I
class TeoriaTwentySix(QtWidgets.QMainWindow,Ui_Teoria26Window):
    def __init__(self):
        super(TeoriaTwentySix, self).__init__()
        self.setupUi(self)
        self.btn_dalee26.clicked.connect(self.onTeoriaTwentySeven)
        self.btn_glavnaya26.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie26.clicked.connect(self.oglavlenie)
        self.btn_return26.clicked.connect(self.returnTeoriaTwentyFive)

    # переход к экрану 'теория 27'
    def onTeoriaTwentySeven(self):
        self.teoria_twenty_seven = TeoriaTwentySeven()
        self.teoria_twenty_seven.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'теория 25' категории I
    def returnTeoriaTwentyFive(self):
        self.T25I = TeoriaTwentyFive()
        self.T25I.show()
        self.hide()

#экран 'теория 27' категории I
class TeoriaTwentySeven(QtWidgets.QMainWindow,Ui_Teoria27Window):
    def __init__(self):
        super(TeoriaTwentySeven, self).__init__()
        self.setupUi(self)

        self.btn_dalee27.clicked.connect(self.onTeoriaTwentyEight)
        self.btn_glavnaya27.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie27.clicked.connect(self.oglavlenie)
        self.btn_return27.clicked.connect(self.returnTeoriaTwentySix)

    # переход к экрану 'теория 28'
    def onTeoriaTwentyEight(self):
        self.teoria_twenty_eight = TeoriaTwentyEight()
        self.teoria_twenty_eight.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'теория 26' категории I
    def returnTeoriaTwentySix(self):
        self.T26I = TeoriaTwentySix()
        self.T26I.show()
        self.hide()

#экран 'теория 28' категории I
class TeoriaTwentyEight(QtWidgets.QMainWindow,Ui_Teoria28Window):
    def __init__(self):
        super(TeoriaTwentyEight, self).__init__()
        self.setupUi(self)

        self.btn_dalee28.clicked.connect(self.onTeoriaTwentyNine)
        self.btn_glavnaya28.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie28.clicked.connect(self.oglavlenie)
        self.btn_return28.clicked.connect(self.returnTeoriaTwentySeven)

        # переход к экрану 'теория 29'
    def onTeoriaTwentyNine(self):
        self.teoria_twenty_nine = TeoriaTwentyNine()
        self.teoria_twenty_nine.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'теория 27' категории I
    def returnTeoriaTwentySeven(self):
        self.T27I = TeoriaTwentySeven()
        self.T27I.show()
        self.hide()

#экран 'теория 29' категория I
class TeoriaTwentyNine(QtWidgets.QMainWindow,Ui_Teoria29Window):
    def __init__(self):
        super(TeoriaTwentyNine, self).__init__()
        self.setupUi(self)

        self.btn_dalee29.clicked.connect(self.onTeoriaThirty)
        self.btn_glavnaya29.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie29.clicked.connect(self.oglavlenie)
        self.btn_return29.clicked.connect(self.returnTeoriaTwentyEight)

    # переход к экрану 'теория 30'
    def onTeoriaThirty(self):
        self.teoria_thirty = TeoriaThirty()
        self.teoria_thirty.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'теория 28' категории I
    def returnTeoriaTwentyEight(self):
        self.T29I = TeoriaTwentyEight()
        self.T29I.show()
        self.hide()

#экран 'теория 30' категория I
class TeoriaThirty(QtWidgets.QMainWindow,Ui_Teoria30Window):
    def __init__(self):
        super(TeoriaThirty, self).__init__()
        self.setupUi(self)

        self.btn_dalee30.clicked.connect(self.onTeoriaThirtyOne)
        self.btn_glavnaya30.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie30.clicked.connect(self.oglavlenie)
        self.btn_return30.clicked.connect(self.returnTeoriaTwentyNine)

    # переход к экрану 'теория 31'
    def onTeoriaThirtyOne(self):
        self.teoria_thirty_one = TeoriaThirtyOne()
        self.teoria_thirty_one.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'теория 29' категории I
    def returnTeoriaTwentyNine(self):
        self.T30I = TeoriaTwentyNine()
        self.T30I.show()
        self.hide()

#экран 'теория 31' категория I
class TeoriaThirtyOne(QtWidgets.QMainWindow,Ui_Teoria31Window):
    def __init__(self):
        super(TeoriaThirtyOne, self).__init__()
        self.setupUi(self)

        self.btn_dalee31.clicked.connect(self.onTeoriaThirtyTwo)
        self.btn_glavnaya31.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie31.clicked.connect(self.oglavlenie)
        self.btn_return31.clicked.connect(self.returnTeoriaThirty)

    # переход к экрану 'теория 32'
    def onTeoriaThirtyTwo(self):
        self.teoria_thirty_two = TeoriaThirtyTwo()
        self.teoria_thirty_two.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'теория 30' категории I
    def returnTeoriaThirty(self):
        self.T31I = TeoriaThirty()
        self.T31I.show()
        self.hide()

#экран 'теория 32' категория I
class TeoriaThirtyTwo(QtWidgets.QMainWindow,Ui_Teoria32Window):
    def __init__(self):
        super(TeoriaThirtyTwo, self).__init__()
        self.setupUi(self)

        self.btn_dalee32.clicked.connect(self.onTeoriaThirtyThree)
        self.btn_glavnaya32.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie32.clicked.connect(self.oglavlenie)
        self.btn_return32.clicked.connect(self.returnTeoriaThirtyOne)

    # переход к экрану 'теория 33'
    def onTeoriaThirtyThree(self):
        self.teoria_thirty_three = TeoriaThirtyThree()
        self.teoria_thirty_three.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'теория 31' категории I
    def returnTeoriaThirtyOne(self):
        self.T32I = TeoriaThirtyOne()
        self.T32I.show()
        self.hide()

#экран 'теория 33' категория I
class TeoriaThirtyThree(QtWidgets.QMainWindow,Ui_Teoria33Window):
    def __init__(self):
        super(TeoriaThirtyThree, self).__init__()
        self.setupUi(self)

        self.btn_dalee33.clicked.connect(self.onTeoriaThirtyFour)
        self.btn_glavnaya33.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie33.clicked.connect(self.oglavlenie)
        self.btn_return33.clicked.connect(self.returnTeoriaThirtyTwo)

    # переход к экрану 'теория 34'
    def onTeoriaThirtyFour(self):
        self.teoria_thirty_four = TeoriaThirtyFour()
        self.teoria_thirty_four.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'теория 32' категории I
    def returnTeoriaThirtyTwo(self):
        self.T33I = TeoriaThirtyTwo()
        self.T33I.show()
        self.hide()

#экран 'теория 34' категория I
class TeoriaThirtyFour(QtWidgets.QMainWindow,Ui_Teoria34Window):
    def __init__(self):
        super(TeoriaThirtyFour, self).__init__()
        self.setupUi(self)

        self.btn_dalee34.clicked.connect(self.onTeoriaThirtyFive)
        self.btn_glavnaya34.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie34.clicked.connect(self.oglavlenie)
        self.btn_return34.clicked.connect(self.returnTeoriaThirtyThree)

    # переход к экрану 'теория 35'
    def onTeoriaThirtyFive(self):
        self.teoria_thirty_five = TeoriaThirtyFive()
        self.teoria_thirty_five.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'теория 33' категории I
    def returnTeoriaThirtyThree(self):
        self.T34I = TeoriaThirtyThree()
        self.T34I.show()
        self.hide()

#экран 'теория 35' категория I
class TeoriaThirtyFive(QtWidgets.QMainWindow,Ui_Teoria35Window):
    def __init__(self):
        super(TeoriaThirtyFive, self).__init__()
        self.setupUi(self)

        self.btn_dalee35.clicked.connect(self.onTeoriaThirtySix)
        self.btn_glavnaya35.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie35.clicked.connect(self.oglavlenie)
        self.btn_return35.clicked.connect(self.returnTeoriaThirtyFour)

    # переход к экрану 'теория 36'
    def onTeoriaThirtySix(self):
        self.teoria_thirty_six = TeoriaThirtySix()
        self.teoria_thirty_six.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'теория 34' категории I
    def returnTeoriaThirtyFour(self):
        self.T35I = TeoriaThirtyFour()
        self.T35I.show()
        self.hide()

#экран 'теория 36' категория I
class TeoriaThirtySix(QtWidgets.QMainWindow,Ui_Teoria36Window):
    def __init__(self):
        super(TeoriaThirtySix, self).__init__()
        self.setupUi(self)

        self.btn_dalee36.clicked.connect(self.onTeoriaThirtySeven)
        self.btn_glavnaya36.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie36.clicked.connect(self.oglavlenie)
        self.btn_return36.clicked.connect(self.returnTeoriaThirtyFive)

    # переход к экрану 'теория 37'
    def onTeoriaThirtySeven(self):
        self.teoria_thirty_seven = TeoriaThirtySeven()
        self.teoria_thirty_seven.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'теория 35' категории I
    def returnTeoriaThirtyFive(self):
        self.T36I = TeoriaThirtyFive()
        self.T36I.show()
        self.hide()

#экран 'теория 37' категория I
class TeoriaThirtySeven(QtWidgets.QMainWindow,Ui_Teoria37Window):
    def __init__(self):
        super(TeoriaThirtySeven, self).__init__()
        self.setupUi(self)

        self.btn_dalee37.clicked.connect(self.onTeoriaThirtyEight)
        self.btn_glavnaya37.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie37.clicked.connect(self.oglavlenie)
        self.btn_return37.clicked.connect(self.returnTeoriaThirtySix)

    # переход к экрану 'теория 38'
    def onTeoriaThirtyEight(self):
        self.teoria_thirty_eight = TeoriaThirtyEight()
        self.teoria_thirty_eight.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie = Oglavlenie()
        self.oglavlenie.show()

# переход к экрану 'теория 36' категории I
    def returnTeoriaThirtySix(self):
        self.T37I = TeoriaThirtySix()
        self.T37I.show()
        self.hide()

#экран 'теория 38' категория I
class TeoriaThirtyEight(QtWidgets.QMainWindow,Ui_Teoria38Window):
    def __init__(self):
        super(TeoriaThirtyEight, self).__init__()
        self.setupUi(self)

        self.btn_dalee38.clicked.connect(self.onTeoriaThirtyNine)
        self.btn_glavnaya38.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie38.clicked.connect(self.oglavlenie)
        self.btn_return38.clicked.connect(self.returnTeoriaThirtySeven)

    # переход к экрану 'теория 39'
    def onTeoriaThirtyNine(self):
        self.teoria_thirty_nine = TeoriaThirtyNine()
        self.teoria_thirty_nine.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'теория 38' категории I
    def returnTeoriaThirtySeven(self):
        self.T38I = TeoriaThirtySeven()
        self.T38I.show()
        self.hide()

#экран 'теория 39' категория I
class TeoriaThirtyNine(QtWidgets.QMainWindow,Ui_Teoria39Window):
    def __init__(self):
        super(TeoriaThirtyNine, self).__init__()
        self.setupUi(self)

        self.btn_glavnaya39.clicked.connect(self.returnGlavnayaI)
        self.btn_oglavlenie39.clicked.connect(self.oglavlenie)
        self.btn_return39.clicked.connect(self.returnTeoriaThirtyEight)

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenie(self):
        self.oglavlenie_ = Oglavlenie()
        self.oglavlenie_.show()

# переход к экрану 'теория 38' категории I
    def returnTeoriaThirtyEight(self):
        self.T39I = TeoriaThirtyEight()
        self.T39I.show()
        self.hide()

#экран 'начать обучение и контроль' категории I
class TestPrompt_0I(QtWidgets.QMainWindow,Ui_TestPrompt0IWindow):
    def __init__(self):
        super(TestPrompt_0I, self).__init__()
        self.setupUi(self)

        self.btn_begin_testprompt.clicked.connect(self.begin_testprompt)
        self.btn_glavnaya_testprompt.clicked.connect(self.returnGlavnayaI)

    def begin_testprompt(self):
        global addressprompt_one
        addressprompt_one = 0
        global numberprompt_one
        numberprompt_one = 0
        global resultprompt_one
        resultprompt_one = 0
        self.testPrompt = TestPromptI()
        self.testPrompt.show()
        self.close()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

#экран вопросы 'обучение и контроль' категории I
class TestPromptI(QtWidgets.QMainWindow,Ui_TestPromptWindow):
    def __init__(self):
        super(TestPromptI, self).__init__()
        self.setupUi(self)
        self.choice_question_answers()
        #функция кнопки ДАЛЕЕ
        self.btn_dalee_testprompt.clicked.connect(self.check_answer)
        #функция кнопки НА ГЛАВНУЮ
        self.btn_glavnaya_testprompt.clicked.connect(self.returnGlavnaya)
        #функция кнопки СПИСОК ВОПРОСОВ
        self.btn_oglavlenie_testprompt.clicked.connect(self.listquestions)

    #вернуться на 'Главную I'
    def returnGlavnaya(self):
        self.return_glavnaya = Glavnaya_I()
        self.return_glavnaya.show()
        self.close()

    #открыть СПИСОК ВОПРОСОВ
    def listquestions(self):
        self.list_questions = QuestionsI()
        self.list_questions.show()
        self.hide()

    #функция вывода вопросов по порядку (ответы перемешиваются)
    def choice_question_answers(self):
        global addressprompt_one
        global numberprompt_one
        numberprompt_one += 1
        question = questionsI[addressprompt_one]
        answers = question_answer[question]
        answer = random.sample(answers, len(answers))
        self.textQuestion.setText(question)
        self.checkBox_1.setText(answer[0]+';')
        self.checkBox_2.setText(answer[1]+';')
        self.checkBox_3.setText(answer[2]+';')
        self.checkBox_4.setText(answer[3]+'.')
        self.labelPrompt.setText(f'Вопрос № {numberprompt_one}')
        if addressprompt_one == 0:
            #1
            self.btn_prompt.clicked.connect(self.onTeoria1)
        elif addressprompt_one ==1:
            #2
            self.btn_prompt.clicked.connect(self.onTeoria1)
        elif addressprompt_one == 2:
            #3
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_one == 3:
            #4
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_one ==4:
            #5
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_one ==5:
            #6
            self.btn_prompt.clicked.connect(self.onTeoria4)
        elif addressprompt_one == 6:
            #7
            self.btn_prompt.clicked.connect(self.onTeoria5)
        elif addressprompt_one == 7:
            #8
            self.btn_prompt.clicked.connect(self.onTeoria6)
        elif addressprompt_one == 8:
            #9
            self.btn_prompt.clicked.connect(self.onTeoria7)
        elif addressprompt_one == 9:
            #10
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_one == 10:
            #11
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_one == 11:
            #12
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_one == 12:
            #13
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_one == 13:
            #14
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_one == 14:
            #15
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 15:
            #16
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 16:
            #17
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 17:
            #18
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 18:
            #19
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 19:
            #20
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 20:
            #21
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 21:
            #22
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_one == 22:
            #23
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_one == 23:
            #24
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_one == 24:
            #25
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_one == 25:
            #26
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 26:
            #27
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 27:
            #28
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 28:
            #29
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 29:
            #30
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 30:
            #31
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 31:
            #32
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 32:
            #33
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_one == 33:
            #34
            self.btn_prompt.clicked.connect(self.onTeoria12)
        elif addressprompt_one == 34:
            #35
            self.btn_prompt.clicked.connect(self.onTeoria12)
        elif addressprompt_one == 35:
            #36
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_one == 36:
            #37
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_one == 37:
            #38
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_one == 38:
            #39
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_one == 39:
            #40
            self.btn_prompt.clicked.connect(self.onTeoria14)
        elif addressprompt_one == 40:
            #41
            self.btn_prompt.clicked.connect(self.onTeoria14)
        elif addressprompt_one == 41:
            #42
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_one == 42:
            #43
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_one == 43:
            #44
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_one == 44:
            #45
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_one == 45:
            #46
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_one == 46:
            #47
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_one == 47:
            #48
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_one == 48:
            #49
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_one == 49:
            #50
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_one == 50:
            #51
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_one == 51:
            #52
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_one == 52:
            #53
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_one == 53:
            #54
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_one == 54:
            #55
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_one == 55:
            #56
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_one == 56:
            #57
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_one == 57:
            #58
            self.btn_prompt.clicked.connect(self.onTeoria18)
        elif addressprompt_one == 58:
            #59
            self.btn_prompt.clicked.connect(self.onTeoria18)
        elif addressprompt_one == 59:
            #60
            self.btn_prompt.clicked.connect(self.onTeoria18)
        elif addressprompt_one == 60:
            #61
            self.btn_prompt.clicked.connect(self.onTeoria19)
        elif addressprompt_one == 61:
            #62
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_one == 62:
            #63
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_one == 63:
            #64
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_one == 64:
            #65
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_one == 65:
            #66
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_one == 66:
            #67
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_one == 67:
            #68
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_one == 68:
            #69
            self.btn_prompt.clicked.connect(self.onTeoria21)
        elif addressprompt_one == 69:
            #70
            self.btn_prompt.clicked.connect(self.onTeoria21)
        elif addressprompt_one == 70:
            #71
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_one == 71:
            #72
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_one == 72:
            #73
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_one == 73:
            #74
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_one == 74:
            #75
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_one == 75:
            #76
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_one == 76:
            #77
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_one == 77:
            #78
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_one == 78:
            #79
            self.btn_prompt.clicked.connect(self.onTeoria24)
        elif addressprompt_one == 79:
            #80
            self.btn_prompt.clicked.connect(self.onTeoria25)
        elif addressprompt_one == 80:
            #81
            self.btn_prompt.clicked.connect(self.onTeoria25)
        elif addressprompt_one == 81:
            #82
            self.btn_prompt.clicked.connect(self.onTeoria25)
        elif addressprompt_one == 82:
            #83
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 83:
            #84
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 84:
            #85
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 85:
            #86
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 86:
            #87
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 87:
            #88
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 88:
            #89
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 89:
            #90
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 90:
            #91
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 91:
            #92
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 92:
            #93
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 93:
            #94
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_one == 94:
            #95
            self.btn_prompt.clicked.connect(self.onTeoria27)
        elif addressprompt_one == 95:
            #96
            self.btn_prompt.clicked.connect(self.onTeoria27)
        elif addressprompt_one == 96:
            #97
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_one == 97:
            #98
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_one == 98:
            #99
            self.btn_prompt.clicked.connect(self.onTeoria28)
        elif addressprompt_one == 99:
            #100
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_one == 100:
            #101
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_one == 101:
            #102
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_one == 102:
            #103
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_one == 103:
            #104
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_one == 104:
            #105
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_one == 105:
            #106
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_one == 106:
            #107
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_one == 107:
            #108
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_one == 108:
            #109
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_one == 109:
            #110
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_one == 110:
            #111
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_one == 111:
            #112
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_one == 112:
            #113
            self.btn_prompt.clicked.connect(self.onTeoria33)
        elif addressprompt_one == 113:
            #114
            self.btn_prompt.clicked.connect(self.onTeoria34)
        elif addressprompt_one == 114:
            #115
            self.btn_prompt.clicked.connect(self.onTeoria34)
        elif addressprompt_one == 115:
            #116
            self.btn_prompt.clicked.connect(self.onTeoria34)
        elif addressprompt_one == 116:
            #117
            self.btn_prompt.clicked.connect(self.onTeoria35)
        elif addressprompt_one == 117:
            #118
            self.btn_prompt.clicked.connect(self.onTeoria35)
        elif addressprompt_one == 118:
            #119
            self.btn_prompt.clicked.connect(self.onTeoria36)
        elif addressprompt_one == 119:
            #120
            self.btn_prompt.clicked.connect(self.onTeoria36)
        elif addressprompt_one == 120:
            #121
            self.btn_prompt.clicked.connect(self.onTeoria37)
        elif addressprompt_one == 121:
            #122
            self.btn_prompt.clicked.connect(self.onTeoria37)
        elif addressprompt_one == 122:
            #123
            self.btn_prompt.clicked.connect(self.onTeoria37)
        elif addressprompt_one == 123:
            #124
            self.btn_prompt.clicked.connect(self.onTeoria38)
        elif addressprompt_one == 124:
            #125
            self.btn_prompt.clicked.connect(self.onTeoria38)
        elif addressprompt_one == 125:
            #126
            self.btn_prompt.clicked.connect(self.onTeoria38)
        elif addressprompt_one == 126:
            #127
            self.btn_prompt.clicked.connect(self.onTeoria38)
        elif addressprompt_one == 127:
            #128
            self.btn_prompt.clicked.connect(self.onTeoria39)
        elif addressprompt_one == 128:
            #129
            self.btn_prompt.clicked.connect(self.onTeoria39)
        addressprompt_one +=1

    def onTeoria1(self):
        self.teoria_vp1 = TeoriaOne()
        self.teoria_vp1.show()

    def onTeoria2(self):
        self.teoria_vp2 = TeoriaTwo()
        self.teoria_vp2.show()

    def onTeoria3(self):
        self.teoria_vp3 = TeoriaThree()
        self.teoria_vp3.show()

    def onTeoria4(self):
        self.teoria_vp4 = TeoriaFour()
        self.teoria_vp4.show()

    def onTeoria5(self):
        self.teoria_vp5 = TeoriaFive()
        self.teoria_vp5.show()

    def onTeoria6(self):
        self.teoria_vp6 = TeoriaSix()
        self.teoria_vp6.show()

    def onTeoria7(self):
        self.teoria_vp7 = TeoriaSeven()
        self.teoria_vp7.show()

    def onTeoria8(self):
        self.teoria_vp8 = TeoriaEight()
        self.teoria_vp8.show()

    def onTeoria9(self):
        self.teoria_vp9 = TeoriaNine()
        self.teoria_vp9.show()

    def onTeoria10(self):
        self.teoria_vp10 = TeoriaTen()
        self.teoria_vp10.show()

    def onTeoria11(self):
        self.teoria_vp11 = TeoriaEleven()
        self.teoria_vp11.show()

    def onTeoria12(self):
        self.teoria_vp12 = TeoriaTwelve()
        self.teoria_vp12.show()

    def onTeoria13(self):
        self.teoria_vp13 = TeoriaThirteen()
        self.teoria_vp13.show()

    def onTeoria14(self):
        self.teoria_vp14 = TeoriaFourteen()
        self.teoria_vp14.show()

    def onTeoria15(self):
        self.teoria_vp15 = TeoriaFifteen()
        self.teoria_vp15.show()

    def onTeoria16(self):
        self.teoria_vp16 = TeoriaSixteen()
        self.teoria_vp16.show()

    def onTeoria17(self):
        self.teoria_vp17 = TeoriaSeventeen()
        self.teoria_vp17.show()

    def onTeoria18(self):
        self.teoria_vp18 = TeoriaEighteen()
        self.teoria_vp18.show()

    def onTeoria19(self):
        self.teoria_vp19 = TeoriaNineteen()
        self.teoria_vp19.show()

    def onTeoria20(self):
        self.teoria_vp20 = TeoriaTwenty()
        self.teoria_vp20.show()

    def onTeoria21(self):
        self.teoria_vp21 = TeoriaTwentyOne()
        self.teoria_vp21.show()

    def onTeoria22(self):
        self.teoria_vp22 = TeoriaTwentyTwo()
        self.teoria_vp22.show()

    def onTeoria23(self):
        self.teoria_vp23 = TeoriaTwentyThree()
        self.teoria_vp23.show()

    def onTeoria24(self):
        self.teoria_vp24 = TeoriaTwentyFour()
        self.teoria_vp24.show()

    def onTeoria25(self):
        self.teoria_vp25 = TeoriaTwentyFive()
        self.teoria_vp25.show()

    def onTeoria26(self):
        self.teoria_vp26 = TeoriaTwentySix()
        self.teoria_vp26.show()

    def onTeoria27(self):
        self.teoria_vp27 = TeoriaTwentySeven()
        self.teoria_vp27.show()

    def onTeoria28(self):
        self.teoria_vp28 = TeoriaTwentyEight()
        self.teoria_vp28.show()

    def onTeoria29(self):
        self.teoria_vp29 = TeoriaTwentyNine()
        self.teoria_vp29.show()

    def onTeoria30(self):
        self.teoria_vp30 = TeoriaThirty()
        self.teoria_vp30.show()

    def onTeoria31(self):
        self.teoria_vp31 = TeoriaThirtyOne()
        self.teoria_vp31.show()

    def onTeoria32(self):
        self.teoria_vp32 = TeoriaThirtyTwo()
        self.teoria_vp32.show()

    def onTeoria33(self):
        self.teoria_vp33 = TeoriaThirtyThree()
        self.teoria_vp33.show()

    def onTeoria34(self):
        self.teoria_vp34 = TeoriaThirtyFour()
        self.teoria_vp34.show()

    def onTeoria35(self):
        self.teoria_vp35 = TeoriaThirtyFive()
        self.teoria_vp35.show()

    def onTeoria36(self):
        self.teoria_vp36 = TeoriaThirtySix()
        self.teoria_vp36.show()

    def onTeoria37(self):
        self.teoria_vp37 = TeoriaThirtySeven()
        self.teoria_vp37.show()

    def onTeoria38(self):
        self.teoria_vp38 = TeoriaThirtyEight()
        self.teoria_vp38.show()

    def onTeoria39(self):
        self.teoria_vp39 = TeoriaThirtyNine()
        self.teoria_vp39.show()

    #очистить выбор checkbox
    def clear(self):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)

    #подсчет правильных ответов
    def check_answer(self):
       if self.checkBox_1.text() in correct_answer and self.checkBox_2.text() in correct_answer:
           if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() == True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_1.text() in correct_answer and self.checkBox_3.text() in correct_answer:
           if self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() == True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_1.text() in correct_answer and self.checkBox_4.text() in correct_answer:
           if self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() == True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_2.text() in correct_answer and self.checkBox_3.text() in correct_answer:
           if self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() == True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_2.text() in correct_answer and self.checkBox_4.text() in correct_answer:
           if self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() == True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_3.text() in correct_answer and self.checkBox_4.text() in correct_answer:
           if self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() == True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_1.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
           if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_2.text() in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
           if self.checkBox_2.isChecked() == True and self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_3.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
           if self.checkBox_3.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() != True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()
       elif self.checkBox_4.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_1.text() not in correct_answer:
           if self.checkBox_4.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_1.isChecked() != True:
               self.right()
               self.clear()
               self.quantity_question()
           else:
               self.wrong()
               self.clear()

    #вывод экрана при нажатии ДАЛЕЕ
    def quantity_question(self):
        if numberprompt_one < 129:
            self.choice_question_answers()
        elif numberprompt_one == 129:
            self.resultatWindow()

    #экран 'Результат'
    def resultatWindow(self):
        self.RWindow = ResultatPromptI()
        self.RWindow.show()
        self.close()

    #диалоговое окно ВЕРНО
    def right(self):
        self.onRight = Right()
        self.onRight.show()
    #диалоговое окно НЕВЕРНО
    def wrong(self):
        self.onWrong = Wrong()
        self.onWrong.show()

#окно 'Результат' режима 'Обучение и контроль'
class ResultatPromptI(QtWidgets.QMainWindow,Ui_ResultatPromWindow):
    def __init__(self):
        super(ResultatPromptI, self).__init__()
        self.setupUi(self)

        self.btn_glavnaya.clicked.connect(self.returnGlavnayaI)
        self.btn_again.clicked.connect(self.onAgainPrompt)

    def onAgainPrompt(self):
        self.on_again = TestPrompt_0I()
        self.on_again.show()
        self.close()

    def returnGlavnayaI(self):
        self.return_glavnayaI = Glavnaya_I()
        self.return_glavnayaI.show()
        self.close()

#экран 'начать контрольный тест'
class Test_0I(QtWidgets.QMainWindow,Ui_Test0Window):
    def __init__(self):
        super(Test_0I, self).__init__()
        self.setupUi(self)

        self.btn_begin_test.clicked.connect(self.begin_test)
        self.btn_glavnaya_test.clicked.connect(self.returnGlavnayaI)

    def begin_test(self):
        global number_one
        number_one = 0
        global result_one
        result_one = 0
        self.test_1 = TestI()
        self.test_1.show()
        self.close()

# переход к экрану 'главная I'
    def returnGlavnayaI(self):
        self.GI = Glavnaya_I()
        self.GI.show()
        self.close()

#экран вопросы 'контрольный тест'
class TestI(QtWidgets.QMainWindow,Ui_TestWindow):
    def __init__(self):
        super(TestI, self).__init__()
        self.setupUi(self)
        self.choice_question_answers()

        self.btn_dalee_test.clicked.connect(self.check_answer)
        self.btn_glavnaya_test.clicked.connect(self.returnGlavnaya)

    def returnGlavnaya(self):
        self.return_glavnaya = Glavnaya_I()
        self.return_glavnaya.show()
        self.close()

    def clear(self):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)

    def choice_question_answers(self):
        question = random.choice(questionsI)
        answers = question_answer[question]
        answer = random.sample(answers, len(answers))
        self.textQuestion.setText(question)
        self.checkBox_1.setText(answer[0]+';')
        self.checkBox_2.setText(answer[1]+';')
        self.checkBox_3.setText(answer[2]+';')
        self.checkBox_4.setText(answer[3]+'.')
        global number_one
        number_one = number_one + 1
        self.label.setText(f'Вопрос № {number_one}')

    def check_answer(self):
        global result_one
        if self.checkBox_1.text() in correct_answer and self.checkBox_2.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() == True:
                result_one +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True:
                result_one +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_2.isChecked() == True:
                result_one +=0.5
            else:
                result_one +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() == True:
                result_one +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() != True:
                result_one +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() == True:
                result_one +=0.5
            else:
                result_one +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() == True:
               result_one +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() != True:
               result_one +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() == True:
               result_one +=0.5
            else:
                result_one +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() == True:
                result_one +=1
            elif self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() != True:
                result_one +=0.5
            elif self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() == True:
                result_one +=0.5
            else:
                result_one +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_one +=1
            elif self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_one +=0.5
            elif self.checkBox_2.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_one +=0.5
            else:
                result_one +=0
        elif self.checkBox_3.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_one +=1
            elif self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_one +=0.5
            elif self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_one +=0.5
            else:
                result_one +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_one +=1
            else:
                result_one +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_one +=1
            else:
                result_one +=0
        elif self.checkBox_3.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_one +=1
            else:
                result_one +=0
        elif self.checkBox_4.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_1.text() not in correct_answer:
            if self.checkBox_4.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_1.isChecked() != True:
                result_one +=1
            else:
                result_one +=0
        print(result_one)
        self.clear()
        self.quantity_question()

    def quantity_question(self):
        if number_one < 20:
            self.choice_question_answers()
        elif number_one == 20:
            self.resultatWindow()

    def resultatWindow(self):
        self.RWindow = ResultatI()
        self.RWindow.show()
        self.close()

#экран 'результат контрольного теста'
class ResultatI(QtWidgets.QMainWindow,Ui_ResultatWindow):
    def __init__(self):
        super(ResultatI, self).__init__()
        self.setupUi(self)
        self.result.setText(str(result_one) + ' из 20.0')


        self.btn_glavnaya.clicked.connect(self.returnGlavnayaI)
        self.btn_again.clicked.connect(self.onAgain)

    def onAgain(self):
        self.on_again = Test_0I()
        self.on_again.show()
        self.close()

    def returnGlavnayaI(self):
        self.return_glavnayaI = Glavnaya_I()
        self.return_glavnayaI.show()
        self.close()

#экран 'оглавление' категории I
class Oglavlenie(QtWidgets.QMainWindow,Ui_OglavlenieWindow):
    def __init__(self):
        super(Oglavlenie, self).__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.on_1)
        self.btn_2.clicked.connect(self.on_2)
        self.btn_3.clicked.connect(self.on_3)
        self.btn_4.clicked.connect(self.on_4)
        self.btn_5.clicked.connect(self.on_5)
        self.btn_6.clicked.connect(self.on_6)
        self.btn_7.clicked.connect(self.on_7)
        self.btn_8.clicked.connect(self.on_8)
        self.btn_9.clicked.connect(self.on_9)
        self.btn_10.clicked.connect(self.on_10)
        self.btn_11.clicked.connect(self.on_11)
        self.btn_12.clicked.connect(self.on_12)
        self.btn_13.clicked.connect(self.on_13)
        self.btn_14.clicked.connect(self.on_14)
        self.btn_15.clicked.connect(self.on_15)
        self.btn_16.clicked.connect(self.on_16)
        self.btn_17.clicked.connect(self.on_17)
        self.btn_18.clicked.connect(self.on_18)
        self.btn_19.clicked.connect(self.on_19)

    def on_1(self): #общие положения
        self.teoria_1 = TeoriaOne()
        self.teoria_1.show()
        self.close()

    def on_2(self): #краткое описание котлоагрегата
        self.teoria_2 = TeoriaThree()
        self.teoria_2.show()
        self.close()

    def on_3(self):#рвп
        self.teoria_3 = TeoriaFour()
        self.teoria_3.show()
        self.close()

    def on_4(self):# тягодутьевая установка
        self.teoria_4 = TeoriaSix()
        self.teoria_4.show()
        self.close()

    def on_5(self):#горелочные устройства
        self.teoria_5 = TeoriaSeven()
        self.teoria_5.show()
        self.close()

    def on_6(self):#паровой тракт
        self.teoria_6 = TeoriaNine()
        self.teoria_6.show()
        self.close()

    def on_7(self):#регулирование температуры
        self.teoria_7 = TeoriaEleven()
        self.teoria_7.show()
        self.close()

    def on_8(self):#описание парового тракта
        self.teoria_8 = TeoriaThirteen()
        self.teoria_8.show()
        self.close()

    def on_9(self):#экономайзер - нрч
        self.teoria_9 = TeoriaFourteen()
        self.teoria_9.show()
        self.close()

    def on_10(self):#срч-врч
        self.teoria_10 = TeoriaSixteen()
        self.teoria_10.show()
        self.close()

    def on_11(self):#встроенные сепараторы
        self.teoria_11 = TeoriaSeventeen()
        self.teoria_11.show()
        self.close()

    def on_12(self):#первичный перегрев
        self.teoria_12 = TeoriaNineteen()
        self.teoria_12.show()
        self.close()

    def on_13(self):#кпп-гпз
        self.teoria_13 = TeoriaTwenty()
        self.teoria_13.show()
        self.close()

    def on_14(self):#вторичный перегрев
        self.teoria_14 = TeoriaTwentyTwo()
        self.teoria_14.show()
        self.close()

    def on_15(self):#защиты и  блокировки
        self.teoria_15 = TeoriaTwentyThree()
        self.teoria_15.show()
        self.close()

    def on_16(self):#защиты, действующие на останов
        self.teoria_16 = TeoriaTwentyFive()
        self.teoria_16.show()
        self.close()

    def on_17(self):#защиты, действующие на снижение нагрузки
        self.teoria_17 = TeoriaThirty()
        self.teoria_17.show()
        self.close()

    def on_18(self):#перечень операций по мнижению нагрузки
        self.teoria_18 = TeoriaThirtyTwo()
        self.teoria_18.show()
        self.close()

    def on_19(self):#условия локальных защит
        self.teoria_19 = TeoriaThirtyFour()
        self.teoria_19.show()
        self.close()

#экран 'оглавление' категории II
class OglavlenieII(QtWidgets.QMainWindow,Ui_OglavlenieWindow):
    def __init__(self):
        super(OglavlenieII, self).__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.on_1)
        self.btn_2.clicked.connect(self.on_2)
        self.btn_3.clicked.connect(self.on_3)
        self.btn_4.clicked.connect(self.on_4)
        self.btn_5.clicked.connect(self.on_5)
        self.btn_6.clicked.connect(self.on_6)
        self.btn_7.clicked.connect(self.on_7)
        self.btn_8.clicked.connect(self.on_8)
        self.btn_9.clicked.connect(self.on_9)
        self.btn_10.clicked.connect(self.on_10)
        self.btn_11.clicked.connect(self.on_11)
        self.btn_12.clicked.connect(self.on_12)
        self.btn_13.clicked.connect(self.on_13)
        self.btn_14.clicked.connect(self.on_14)
        self.btn_15.clicked.connect(self.on_15)
        self.btn_16.clicked.connect(self.on_16)
        self.btn_17.clicked.connect(self.on_17)
        self.btn_18.clicked.connect(self.on_18)
        self.btn_19.clicked.connect(self.on_19)

    def on_1(self):  # общие положения
        self.teoria_1II = TeoriaOneII()
        self.teoria_1II.show()
        self.close()

    def on_2(self):  # краткое описание котлоагрегата
        self.teoria_2II = TeoriaThreeII()
        self.teoria_2II.show()
        self.close()

    def on_3(self):  # рвп
        self.teoria_3II = TeoriaFourII()
        self.teoria_3II.show()
        self.close()

    def on_4(self):  # тягодутьевая установка
        self.teoria_4II = TeoriaSixII()
        self.teoria_4II.show()
        self.close()

    def on_5(self):  # горелочные устройства
        self.teoria_5II = TeoriaSevenII()
        self.teoria_5II.show()
        self.close()

    def on_6(self):  # паровой тракт
        self.teoria_6II = TeoriaNineII()
        self.teoria_6II.show()
        self.close()

    def on_7(self):  # регулирование температуры
        self.teoria_7II = TeoriaElevenII()
        self.teoria_7II.show()
        self.close()

    def on_8(self):  # описание парового тракта
        self.teoria_8II = TeoriaThirteenII()
        self.teoria_8II.show()
        self.close()

    def on_9(self):  # экономайзер - нрч
        self.teoria_9II = TeoriaFourteenII()
        self.teoria_9II.show()
        self.close()

    def on_10(self):  # срч-врч
        self.teoria_10II = TeoriaSixteenII()
        self.teoria_10II.show()
        self.close()

    def on_11(self):  # встроенные сепараторы
        self.teoria_11II = TeoriaSeventeenII()
        self.teoria_11II.show()
        self.close()

    def on_12(self):  # первичный перегрев
        self.teoria_12II = TeoriaNineteenII()
        self.teoria_12II.show()
        self.close()

    def on_13(self):  # кпп-гпз
        self.teoria_13II = TeoriaTwentyII()
        self.teoria_13II.show()
        self.close()

    def on_14(self):  # вторичный перегрев
        self.teoria_14II = TeoriaTwentyTwoII()
        self.teoria_14II.show()
        self.close()

    def on_15(self):  # защиты и  блокировки
        self.teoria_15II = TeoriaTwentyThreeII()
        self.teoria_15II.show()
        self.close()

    def on_16(self):  # защиты, действующие на останов
        self.teoria_16II = TeoriaTwentyFiveII()
        self.teoria_16II.show()
        self.close()

    def on_17(self):  # защиты, действующие на снижение нагрузки
        self.teoria_17II = TeoriaThirtyII()
        self.teoria_17II.show()
        self.close()

    def on_18(self):  # перечень операций по мнижению нагрузки
        self.teoria_18II = TeoriaThirtyTwoII()
        self.teoria_18II.show()
        self.close()

    def on_19(self):  # условия локальных защит
        self.teoria_19II = TeoriaThirtyFourII()
        self.teoria_19II.show()
        self.close()

#экран 'оглавление' категории III
class OglavlenieIII(QtWidgets.QMainWindow,Ui_OglavlenieWindow):
    def __init__(self):
        super(OglavlenieIII, self).__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.on_1)
        self.btn_2.clicked.connect(self.on_2)
        self.btn_3.clicked.connect(self.on_3)
        self.btn_4.clicked.connect(self.on_4)
        self.btn_5.clicked.connect(self.on_5)
        self.btn_6.clicked.connect(self.on_6)
        self.btn_7.clicked.connect(self.on_7)
        self.btn_8.clicked.connect(self.on_8)
        self.btn_9.clicked.connect(self.on_9)
        self.btn_10.clicked.connect(self.on_10)
        self.btn_11.clicked.connect(self.on_11)
        self.btn_12.clicked.connect(self.on_12)
        self.btn_13.clicked.connect(self.on_13)
        self.btn_14.clicked.connect(self.on_14)
        self.btn_15.clicked.connect(self.on_15)
        self.btn_16.clicked.connect(self.on_16)
        self.btn_17.clicked.connect(self.on_17)
        self.btn_18.clicked.connect(self.on_18)
        self.btn_19.clicked.connect(self.on_19)

    def on_1(self):  # общие положения
        self.teoria_1III = TeoriaOneIII()
        self.teoria_1III.show()
        self.close()

    def on_2(self):  # краткое описание котлоагрегата
        self.teoria_2III = TeoriaThreeIII()
        self.teoria_2III.show()
        self.close()

    def on_3(self):  # рвп
        self.teoria_3III = TeoriaFourIII()
        self.teoria_3III.show()
        self.close()

    def on_4(self):  # тягодутьевая установка
        self.teoria_4III = TeoriaSixIII()
        self.teoria_4III.show()
        self.close()

    def on_5(self):  # горелочные устройства
        self.teoria_5III = TeoriaSevenIII()
        self.teoria_5III.show()
        self.close()

    def on_6(self):  # паровой тракт
        self.teoria_6III = TeoriaNineIII()
        self.teoria_6III.show()
        self.close()

    def on_7(self):  # регулирование температуры
        self.teoria_7III = TeoriaElevenIII()
        self.teoria_7III.show()
        self.close()

    def on_8(self):  # описание парового тракта
        self.teoria_8III = TeoriaThirteenIII()
        self.teoria_8III.show()
        self.close()

    def on_9(self):  # экономайзер - нрч
        self.teoria_9III = TeoriaFourteenIII()
        self.teoria_9III.show()
        self.close()

    def on_10(self):  # срч-врч
        self.teoria_10III = TeoriaSixteenIII()
        self.teoria_10III.show()
        self.close()

    def on_11(self):  # встроенные сепараторы
        self.teoria_11III = TeoriaSeventeenIII()
        self.teoria_11III.show()
        self.close()

    def on_12(self):  # первичный перегрев
        self.teoria_12III = TeoriaNineteenIII()
        self.teoria_12III.show()
        self.close()

    def on_13(self):  # кпп-гпз
        self.teoria_13III = TeoriaTwentyIII()
        self.teoria_13III.show()
        self.close()

    def on_14(self):  # вторичный перегрев
        self.teoria_14III = TeoriaTwentyTwoIII()
        self.teoria_14III.show()
        self.close()

    def on_15(self):  # защиты и  блокировки
        self.teoria_15III = TeoriaTwentyThreeIII()
        self.teoria_15III.show()
        self.close()

    def on_16(self):  # защиты, действующие на останов
        self.teoria_16III = TeoriaTwentyFiveIII()
        self.teoria_16III.show()
        self.close()

    def on_17(self):  # защиты, действующие на снижение нагрузки
        self.teoria_17III = TeoriaThirtyIII()
        self.teoria_17III.show()
        self.close()

    def on_18(self):  # перечень операций по мнижению нагрузки
        self.teoria_18III = TeoriaThirtyTwoIII()
        self.teoria_18III.show()
        self.close()

    def on_19(self):  # условия локальных защит
        self.teoria_19III = TeoriaThirtyFourIII()
        self.teoria_19III.show()
        self.close()

#экран 'Теория 1' категории II
class TeoriaOneII(QtWidgets.QMainWindow, Ui_Teoria1Window):
    def __init__(self):
        super(TeoriaOneII, self).__init__()
        self.setupUi(self)

        self.btn_dalee1.clicked.connect(self.onTeoriaTwoII)
        self.btn_oglavlenie1.clicked.connect(self.oglavlenieII)
        self.btn_glavnaya1.clicked.connect(self.returnGlavnayaII)

    # переход к экрану 'теория 2' категории II
    def onTeoriaTwoII(self):
        self.teoria_twoII = TeoriaTwoII()
        self.teoria_twoII.show()
        self.hide()

    # переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie_II = OglavlenieII()
        self.oglavlenie_II.show()

    # переход к главному экрану 'теория 2' категории II
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

#экран 'Теория 2' категории II
class TeoriaTwoII(QtWidgets.QMainWindow,Ui_Teoria2Window):
    def __init__(self):
        super(TeoriaTwoII, self).__init__()
        self.setupUi(self)

        self.btn_dalee2.clicked.connect(self.onTeoriaThreeII)
        self.btn_glavnaya2.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie2.clicked.connect(self.oglavlenieII)
        self.btn_return2.clicked.connect(self.returnTeoriaOneII)

#переход к экрану 'теория 3' категории II
    def onTeoriaThreeII(self):
        self.teoria_threeII = TeoriaThreeII()
        self.teoria_threeII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie_II = OglavlenieII()
        self.oglavlenie_II.show()

#переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к главному экрану 'теория 1' категории II
    def returnTeoriaOneII(self):
        self.T1II = TeoriaOneII()
        self.T1II.show()
        self.hide()

#экран 'Теория 3' категории II
class TeoriaThreeII(QtWidgets.QMainWindow,Ui_Teoria3Window):
    def __init__(self):
        super(TeoriaThreeII, self).__init__()
        self.setupUi(self)

        self.btn_dalee3.clicked.connect(self.onTeoriaFourII)
        self.btn_glavnaya3.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie3.clicked.connect(self.oglavlenieII)
        self.btn_return3.clicked.connect(self.returnTeoriaTwoII)

#переход к экрану 'теория 4'
    def onTeoriaFourII(self):
        self.teoria_fourII = TeoriaFourII()
        self.teoria_fourII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie_II = OglavlenieII()
        self.oglavlenie_II.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 2' категории II
    def returnTeoriaTwoII(self):
        self.T2II = TeoriaTwoII()
        self.T2II.show()
        self.hide()

#экран 'теория 4' категории II
class TeoriaFourII(QtWidgets.QMainWindow,Ui_Teoria4Window):
    def __init__(self):
        super(TeoriaFourII, self).__init__()
        self.setupUi(self)

        self.btn_dalee4.clicked.connect(self.onTeoriaFiveII)
        self.btn_glavnaya4.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie4.clicked.connect(self.oglavlenieII)
        self.btn_return4.clicked.connect(self.returnTeoriaThreeII)

# переход к экрану 'теория 5'
    def onTeoriaFiveII(self):
        self.teoria_fiveII = TeoriaFiveII()
        self.teoria_fiveII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

#переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 3' категории II
    def returnTeoriaThreeII(self):
        self.T3II = TeoriaThreeII()
        self.T3II.show()
        self.hide()

#экран 'теория 5' категории II
class TeoriaFiveII(QtWidgets.QMainWindow,Ui_Teoria5Window):
    def __init__(self):
        super(TeoriaFiveII, self).__init__()
        self.setupUi(self)

        self.btn_dalee5.clicked.connect(self.onTeoriaSixII)
        self.btn_glavnaya5.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie5.clicked.connect(self.oglavlenieII)
        self.btn_return5.clicked.connect(self.returnTeoriaFourII)

#переход к экрану 'теория 6'
    def onTeoriaSixII(self):
        self.teoria_sixII = TeoriaSixII()
        self.teoria_sixII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

#переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 4' категории II
    def returnTeoriaFourII(self):
        self.T4II = TeoriaFourII()
        self.T4II.show()
        self.hide()

#экран 'теория 6' категории II
class TeoriaSixII(QtWidgets.QMainWindow,Ui_Teoria6Window):
    def __init__(self):
        super(TeoriaSixII, self).__init__()
        self.setupUi(self)

        self.btn_dalee6.clicked.connect(self.onTeoriaSevenII)
        self.btn_glavnaya6.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie6.clicked.connect(self.oglavlenieII)
        self.btn_return6.clicked.connect(self.returnTeoriaFiveII)

# переход к экрану 'теория 7'
    def onTeoriaSevenII(self):
        self.teoria_sevenII = TeoriaSevenII()
        self.teoria_sevenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 5' категории II
    def returnTeoriaFiveII(self):
        self.T5II = TeoriaFiveII()
        self.T5II.show()
        self.hide()

#экран 'теория 7' категории II
class TeoriaSevenII(QtWidgets.QMainWindow,Ui_Teoria7Window):
    def __init__(self):
        super(TeoriaSevenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee7.clicked.connect(self.onTeoriaEightII)
        self.btn_glavnaya7.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie7.clicked.connect(self.oglavlenieII)
        self.btn_return7.clicked.connect(self.returnTeoriaSixII)

# переход к экрану 'теория 8'
    def onTeoriaEightII(self):
        self.teoria_eightII = TeoriaEightII()
        self.teoria_eightII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 6' категории I
    def returnTeoriaSixII(self):
        self.T6II = TeoriaSixII()
        self.T6II.show()
        self.hide()

#экран 'теория 8' категории II
class TeoriaEightII(QtWidgets.QMainWindow,Ui_Teoria8Window):
    def __init__(self):
        super(TeoriaEightII, self).__init__()
        self.setupUi(self)

        self.btn_dalee8.clicked.connect(self.onTeoriaNineII)
        self.btn_glavnaya8.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie8.clicked.connect(self.oglavlenieII)
        self.btn_return8.clicked.connect(self.returnTeoriaSevenII)

# переход к экрану 'теория 9'
    def onTeoriaNineII(self):
        self.teoria_nineII = TeoriaNineII()
        self.teoria_nineII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная I'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 7' категории I
    def returnTeoriaSevenII(self):
        self.T7II = TeoriaSevenII()
        self.T7II.show()
        self.hide()

#экран 'теория 9' категории II
class TeoriaNineII(QtWidgets.QMainWindow,Ui_Teoria9Window):
    def __init__(self):
        super(TeoriaNineII, self).__init__()
        self.setupUi(self)

        self.btn_dalee9.clicked.connect(self.onTeoriaTenII)
        self.btn_glavnaya9.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie9.clicked.connect(self.oglavlenieII)
        self.btn_return9.clicked.connect(self.returnTeoriaEightII)

# переход к экрану 'теория 10'
    def onTeoriaTenII(self):
        self.teoria_tenII = TeoriaTenII()
        self.teoria_tenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная I'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 8' категории I
    def returnTeoriaEightII(self):
        self.T8II = TeoriaEightII()
        self.T8II.show()
        self.hide()

#экран 'теория 10' категории II
class TeoriaTenII(QtWidgets.QMainWindow,Ui_Teoria10Window):
    def __init__(self):
        super(TeoriaTenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee10.clicked.connect(self.onTeoriaElevenII)
        self.btn_glavnaya10.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie10.clicked.connect(self.oglavlenieII)
        self.btn_return10.clicked.connect(self.returnTeoriaNineII)

# переход к экрану 'теория 11'
    def onTeoriaElevenII(self):
        self.teoria_elevenII = TeoriaElevenII()
        self.teoria_elevenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 9' категории I
    def returnTeoriaNineII(self):
        self.T9II = TeoriaNineII()
        self.T9II.show()
        self.hide()

#экран 'теория 11' категории II
class TeoriaElevenII(QtWidgets.QMainWindow,Ui_Teoria11Window):
    def __init__(self):
        super(TeoriaElevenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee11.clicked.connect(self.onTeoriaTwelveII)
        self.btn_glavnaya11.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie11.clicked.connect(self.oglavlenieII)
        self.btn_return11.clicked.connect(self.returnTeoriaTenII)

# переход к экрану 'теория 12'
    def onTeoriaTwelveII(self):
        self.teoria_twelveII = TeoriaTwelveII()
        self.teoria_twelveII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 10' категории II
    def returnTeoriaTenII(self):
        self.T10II = TeoriaTenII()
        self.T10II.show()
        self.hide()

#экран 'теория 12' категории II
class TeoriaTwelveII(QtWidgets.QMainWindow,Ui_Teoria12Window):
    def __init__(self):
        super(TeoriaTwelveII, self).__init__()
        self.setupUi(self)

        self.btn_dalee12.clicked.connect(self.onTeoriaThirteenII)
        self.btn_glavnaya12.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie12.clicked.connect(self.oglavlenieII)
        self.btn_return12.clicked.connect(self.returnTeoriaElevenII)

# переход к экрану 'теория 13'
    def onTeoriaThirteenII(self):
        self.teoria_thirteenII = TeoriaThirteenII()
        self.teoria_thirteenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 11' категории II
    def returnTeoriaElevenII(self):
        self.T11II = TeoriaElevenII()
        self.T11II.show()
        self.hide()

#экран 'теория 13' категории II
class TeoriaThirteenII(QtWidgets.QMainWindow,Ui_Teoria13Window):
    def __init__(self):
        super(TeoriaThirteenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee13.clicked.connect(self.onTeoriaFourteenII)
        self.btn_glavnaya13.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie13.clicked.connect(self.oglavlenieII)
        self.btn_return13.clicked.connect(self.returnTeoriaTwelveII)

# переход к экрану 'теория 14'
    def onTeoriaFourteenII(self):
        self.teoria_fourteenII = TeoriaFourteenII()
        self.teoria_fourteenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 12' категории II
    def returnTeoriaTwelveII(self):
        self.T12II = TeoriaTwelveII()
        self.T12II.show()
        self.hide()

#экран 'теория 14' категории II
class TeoriaFourteenII(QtWidgets.QMainWindow,Ui_Teoria14Window):
    def __init__(self):
        super(TeoriaFourteenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee14.clicked.connect(self.onTeoriaFifteenII)
        self.btn_glavnaya14.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie14.clicked.connect(self.oglavlenieII)
        self.btn_return14.clicked.connect(self.returnTeoriaThirteenII)

# переход к экрану 'теория 15'
    def onTeoriaFifteenII(self):
        self.teoria_fifteenII = TeoriaFifteenII()
        self.teoria_fifteenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 13' категории II
    def returnTeoriaThirteenII(self):
        self.T13II = TeoriaThirteenII()
        self.T13II.show()
        self.hide()

#экран 'теория 15' категории II
class TeoriaFifteenII(QtWidgets.QMainWindow,Ui_Teoria15Window):
    def __init__(self):
        super(TeoriaFifteenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee15.clicked.connect(self.onTeoriaSixteenII)
        self.btn_glavnaya15.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie15.clicked.connect(self.oglavlenieII)
        self.btn_return15.clicked.connect(self.returnTeoriaFourteenII)

# переход к экрану 'теория 16'
    def onTeoriaSixteenII(self):
        self.teoria_sixteenII = TeoriaSixteenII()
        self.teoria_sixteenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 14' категории I
    def returnTeoriaFourteenII(self):
        self.T14II = TeoriaFourteenII()
        self.T14II.show()
        self.hide()

#экран 'теория 16' каегории II
class TeoriaSixteenII(QtWidgets.QMainWindow,Ui_Teoria16Window):
    def __init__(self):
        super(TeoriaSixteenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee16.clicked.connect(self.onTeoriaSeventeenII)
        self.btn_glavnaya16.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie16.clicked.connect(self.oglavlenieII)
        self.btn_return16.clicked.connect(self.returnTeoriaFifteenII)

# переход к экрану 'теория 17'
    def onTeoriaSeventeenII(self):
        self.teoria_seventeenII = TeoriaSeventeenII()
        self.teoria_seventeenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 15' категории II
    def returnTeoriaFifteenII(self):
        self.T15II = TeoriaFifteenII()
        self.T15II.show()
        self.hide()

#экран 'теория 17' категории II
class TeoriaSeventeenII(QtWidgets.QMainWindow,Ui_Teoria17Window):
    def __init__(self):
        super(TeoriaSeventeenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee17.clicked.connect(self.onTeoriaEighteenII)
        self.btn_glavnaya17.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie17.clicked.connect(self.oglavlenieII)
        self.btn_return17.clicked.connect(self.returnTeoriaSixteenII)

# переход к экрану 'теория 18'
    def onTeoriaEighteenII(self):
        self.teoria_eighteenII = TeoriaEighteenII()
        self.teoria_eighteenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 16' категории II
    def returnTeoriaSixteenII(self):
        self.T16II = TeoriaSixteenII()
        self.T16II.show()
        self.hide()

#экран 'теория 18' категории II
class TeoriaEighteenII(QtWidgets.QMainWindow,Ui_Teoria18Window):
    def __init__(self):
        super(TeoriaEighteenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee18.clicked.connect(self.onTeoriaNineteenII)
        self.btn_glavnaya18.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie18.clicked.connect(self.oglavlenieII)
        self.btn_return18.clicked.connect(self.returnTeoriaSeventeenII)

# переход к экрану 'теория 19'
    def onTeoriaNineteenII(self):
        self.teoria_nineteenII = TeoriaNineteenII()
        self.teoria_nineteenII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 17' категории II
    def returnTeoriaSeventeenII(self):
        self.T17II = TeoriaSeventeenII()
        self.T17II.show()
        self.hide()

#экран 'теория 19' категории II
class TeoriaNineteenII(QtWidgets.QMainWindow,Ui_Teoria19Window):
    def __init__(self):
        super(TeoriaNineteenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee19.clicked.connect(self.onTeoriaTwentyII)
        self.btn_glavnaya19.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie19.clicked.connect(self.oglavlenieII)
        self.btn_return19.clicked.connect(self. returnTeoriaEighteenII)

# переход к экрану 'теория 20'
    def onTeoriaTwentyII(self):
        self.teoria_twentyII = TeoriaTwentyII()
        self.teoria_twentyII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 18' категории II
    def returnTeoriaEighteenII(self):
        self.T18II = TeoriaEighteenII()
        self.T18II.show()
        self.hide()

#экран 'теория 20' категории II
class TeoriaTwentyII(QtWidgets.QMainWindow,Ui_Teoria20Window):
    def __init__(self):
        super(TeoriaTwentyII, self).__init__()
        self.setupUi(self)

        self.btn_dalee20.clicked.connect(self.onTeoriaTwentyOneII)
        self.btn_glavnaya20.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie20.clicked.connect(self.oglavlenieII)
        self.btn_return20.clicked.connect(self.returnTeoriaNineteenII)

# переход к экрану 'теория 21'
    def onTeoriaTwentyOneII(self):
        self.teoria_twenty_oneII = TeoriaTwentyOneII()
        self.teoria_twenty_oneII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 19' категории II
    def returnTeoriaNineteenII(self):
        self.T19II = TeoriaNineteenII()
        self.T19II.show()
        self.hide()

#экран 'теория 21' категории II
class TeoriaTwentyOneII(QtWidgets.QMainWindow,Ui_Teoria21Window):
    def __init__(self):
        super(TeoriaTwentyOneII, self).__init__()
        self.setupUi(self)

        self.btn_dalee21.clicked.connect(self.onTeoriaTwentyTwoII)
        self.btn_glavnaya21.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie21.clicked.connect(self.oglavlenieII)
        self.btn_return21.clicked.connect(self.returnTeoriaTwentyII)

# переход к экрану 'теория 22'
    def onTeoriaTwentyTwoII(self):
        self.teoria_twenty_twoII = TeoriaTwentyTwoII()
        self.teoria_twenty_twoII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 20' категории II
    def returnTeoriaTwentyII(self):
        self.T20II = TeoriaTwentyII()
        self.T20II.show()
        self.hide()

#экран 'теория 22' категории II
class TeoriaTwentyTwoII(QtWidgets.QMainWindow,Ui_Teoria22Window):
    def __init__(self):
        super(TeoriaTwentyTwoII, self).__init__()
        self.setupUi(self)

        self.btn_dalee22.clicked.connect(self.onTeoriaTwentyThreeII)
        self.btn_glavnaya22.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie22.clicked.connect(self.oglavlenieII)
        self.btn_return22.clicked.connect(self.returnTeoriaTwentyOneII)

# переход к экрану 'теория 23'
    def onTeoriaTwentyThreeII(self):
        self.teoria_twenty_threeII = TeoriaTwentyThreeII()
        self.teoria_twenty_threeII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 21' категории II
    def returnTeoriaTwentyOneII(self):
        self.T21II = TeoriaTwentyOneII()
        self.T21II.show()
        self.hide()

#экран 'теория 23' категории II
class TeoriaTwentyThreeII(QtWidgets.QMainWindow,Ui_Teoria23Window):
    def __init__(self):
        super(TeoriaTwentyThreeII, self).__init__()
        self.setupUi(self)

        self.btn_dalee23.clicked.connect(self.onTeoriaTwentyFourII)
        self.btn_glavnaya23.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie23.clicked.connect(self.oglavlenieII)
        self.btn_return23.clicked.connect(self.returnTeoriaTwentyTwoII)

# переход к экрану 'теория 24'
    def onTeoriaTwentyFourII(self):
        self.teoria_twenty_fourII = TeoriaTwentyFourII()
        self.teoria_twenty_fourII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie_II = OglavlenieII()
        self.oglavlenie_II.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 22' категории II
    def returnTeoriaTwentyTwoII(self):
        self.T22II = TeoriaTwentyTwoII()
        self.T22II.show()
        self.hide()

#экран 'теория 24' категории II
class TeoriaTwentyFourII(QtWidgets.QMainWindow,Ui_Teoria24Window):
    def __init__(self):
        super(TeoriaTwentyFourII, self).__init__()
        self.setupUi(self)

        self.btn_dalee24.clicked.connect(self.onTeoriaTwentyFiveII)
        self.btn_glavnaya24.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie24.clicked.connect(self.oglavlenieII)
        self.btn_return24.clicked.connect(self.returnTeoriaTwentyThreeII)

# переход к экрану 'теория 25'
    def onTeoriaTwentyFiveII(self):
        self.teoria_twenty_fiveII = TeoriaTwentyFiveII()
        self.teoria_twenty_fiveII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie_II = OglavlenieII()
        self.oglavlenie_II.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 23' категории II
    def returnTeoriaTwentyThreeII(self):
        self.T23II = TeoriaTwentyThreeII()
        self.T23II.show()
        self.hide()

#экран 'теория 25' категории II
class TeoriaTwentyFiveII(QtWidgets.QMainWindow,Ui_Teoria25Window):
    def __init__(self):
        super(TeoriaTwentyFiveII, self).__init__()
        self.setupUi(self)

        self.btn_dalee25.clicked.connect(self.onTeoriaTwentySixII)
        self.btn_glavnaya25.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie25.clicked.connect(self.oglavlenieII)
        self.btn_return25.clicked.connect(self.returnTeoriaTwentyFourII)

# переход к экрану 'теория 26'
    def onTeoriaTwentySixII(self):
        self.teoria_twenty_sixII = TeoriaTwentySixII()
        self.teoria_twenty_sixII.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie_II = OglavlenieII()
        self.oglavlenie_II.show()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'теория 24' категории II
    def returnTeoriaTwentyFourII(self):
        self.T24II = TeoriaTwentyFourII()
        self.T24II.show()
        self.hide()

#экран 'теория 26'категории II
class TeoriaTwentySixII(QtWidgets.QMainWindow,Ui_Teoria26Window):
    def __init__(self):
        super(TeoriaTwentySixII, self).__init__()
        self.setupUi(self)

        self.btn_dalee26.clicked.connect(self.onTeoriaTwentySevenII)
        self.btn_glavnaya26.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie26.clicked.connect(self.oglavlenieII)
        self.btn_return26.clicked.connect(self.returnTeoriaTwentyFiveII)

    # переход к экрану 'теория 27'
    def onTeoriaTwentySevenII(self):
        self.teoria_twenty_sevenII = TeoriaTwentySevenII()
        self.teoria_twenty_sevenII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'теория 25' категории II
    def returnTeoriaTwentyFiveII(self):
        self.T25II = TeoriaTwentyFiveII()
        self.T25II.show()
        self.hide()

#экран 'теория 27' категории II
class TeoriaTwentySevenII(QtWidgets.QMainWindow,Ui_Teoria27Window):
    def __init__(self):
        super(TeoriaTwentySevenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee27.clicked.connect(self.onTeoriaTwentyEightII)
        self.btn_glavnaya27.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie27.clicked.connect(self.oglavlenieII)
        self.btn_return27.clicked.connect(self.returnTeoriaTwentySix)

    # переход к экрану 'теория 28'
    def onTeoriaTwentyEightII(self):
        self.teoria_twenty_eightII = TeoriaTwentyEightII()
        self.teoria_twenty_eightII.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'теория 26' категории I
    def returnTeoriaTwentySix(self):
        self.T26II = TeoriaTwentySixII()
        self.T26II.show()
        self.hide()

#экран 'теория 28' категории II
class TeoriaTwentyEightII(QtWidgets.QMainWindow,Ui_Teoria28Window):
    def __init__(self):
        super(TeoriaTwentyEightII, self).__init__()
        self.setupUi(self)

        self.btn_dalee28.clicked.connect(self.onTeoriaTwentyNineII)
        self.btn_glavnaya28.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie28.clicked.connect(self.oglavlenieII)
        self.btn_return28.clicked.connect(self.returnTeoriaTwentySeven)

    # переход к экрану 'теория 29'
    def onTeoriaTwentyNineII(self):
        self.teoria_twenty_nineII = TeoriaTwentyNineII()
        self.teoria_twenty_nineII.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'теория 27' категории I
    def returnTeoriaTwentySeven(self):
        self.T27II = TeoriaTwentySevenII()
        self.T27II.show()
        self.hide()

#экран 'теория 29' категория II
class TeoriaTwentyNineII(QtWidgets.QMainWindow,Ui_Teoria29Window):
    def __init__(self):
        super(TeoriaTwentyNineII, self).__init__()
        self.setupUi(self)

        self.btn_dalee29.clicked.connect(self.onTeoriaThirtyII)
        self.btn_glavnaya29.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie29.clicked.connect(self.oglavlenieII)
        self.btn_return29.clicked.connect(self.returnTeoriaTwentyEight)

    # переход к экрану 'теория 30'
    def onTeoriaThirtyII(self):
        self.teoria_thirtyII = TeoriaThirtyII()
        self.teoria_thirtyII.show()
        self.hide()

# переход к экрану 'главная I'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenieII = OglavlenieII()
        self.oglavlenieII.show()

# переход к экрану 'теория 28' категории I
    def returnTeoriaTwentyEight(self):
        self.T29II = TeoriaTwentyEightII()
        self.T29II.show()
        self.hide()

#экран 'теория 30' категория II
class TeoriaThirtyII(QtWidgets.QMainWindow,Ui_Teoria30Window):
    def __init__(self):
        super(TeoriaThirtyII, self).__init__()
        self.setupUi(self)

        self.btn_dalee30.clicked.connect(self.onTeoriaThirtyOneII)
        self.btn_glavnaya30.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie30.clicked.connect(self.oglavlenieII)
        self.btn_return30.clicked.connect(self.returnTeoriaTwentyNine)

    # переход к экрану 'теория 31'
    def onTeoriaThirtyOneII(self):
        self.teoria_thirty_oneII = TeoriaThirtyOneII()
        self.teoria_thirty_oneII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 29' категории II
    def returnTeoriaTwentyNine(self):
        self.T30II = TeoriaTwentyNineII()
        self.T30II.show()
        self.hide()

    # экран 'теория 31' категория II

#экран 'теория 31' категория II
class TeoriaThirtyOneII(QtWidgets.QMainWindow, Ui_Teoria31Window):
    def __init__(self):
        super(TeoriaThirtyOneII, self).__init__()
        self.setupUi(self)

        self.btn_dalee31.clicked.connect(self.onTeoriaThirtyTwoII)
        self.btn_glavnaya31.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie31.clicked.connect(self.oglavlenieII)
        self.btn_return31.clicked.connect(self.returnTeoriaThirty)

    # переход к экрану 'теория 32'
    def onTeoriaThirtyTwoII(self):
        self.teoria_thirty_twoII = TeoriaThirtyTwoII()
        self.teoria_thirty_twoII.show()
        self.hide()

    # переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

    # переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 30' категории II
    def returnTeoriaThirty(self):
        self.T30II = TeoriaThirtyII()
        self.T30II.show()
        self.hide()

#экран 'теория 32' категория II
class TeoriaThirtyTwoII(QtWidgets.QMainWindow,Ui_Teoria32Window):
    def __init__(self):
        super(TeoriaThirtyTwoII, self).__init__()
        self.setupUi(self)

        self.btn_dalee32.clicked.connect(self.onTeoriaThirtyThreeII)
        self.btn_glavnaya32.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie32.clicked.connect(self.oglavlenieII)
        self.btn_return32.clicked.connect(self.returnTeoriaThirtyOne)

    # переход к экрану 'теория 33'
    def onTeoriaThirtyThreeII(self):
        self.teoria_thirty_threeII = TeoriaThirtyThreeII()
        self.teoria_thirty_threeII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 31' категории II
    def returnTeoriaThirtyOne(self):
        self.T32II = TeoriaThirtyOneII()
        self.T32II.show()
        self.hide()

#экран 'теория 33' категория II
class TeoriaThirtyThreeII(QtWidgets.QMainWindow,Ui_Teoria33Window):
    def __init__(self):
        super(TeoriaThirtyThreeII, self).__init__()
        self.setupUi(self)

        self.btn_dalee33.clicked.connect(self.onTeoriaThirtyFourII)
        self.btn_glavnaya33.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie33.clicked.connect(self.oglavlenieII)
        self.btn_return33.clicked.connect(self.returnTeoriaThirtyTwo)

    # переход к экрану 'теория 34'
    def onTeoriaThirtyFourII(self):
        self.teoria_thirty_fourII = TeoriaThirtyFourII()
        self.teoria_thirty_fourII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 32' категории II
    def returnTeoriaThirtyTwo(self):
        self.T33II = TeoriaThirtyTwoII()
        self.T33II.show()
        self.hide()

#экран 'теория 34' категория II
class TeoriaThirtyFourII(QtWidgets.QMainWindow,Ui_Teoria34Window):
    def __init__(self):
        super(TeoriaThirtyFourII, self).__init__()
        self.setupUi(self)

        self.btn_dalee34.clicked.connect(self.onTeoriaThirtyFiveII)
        self.btn_glavnaya34.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie34.clicked.connect(self.oglavlenieII)
        self.btn_return34.clicked.connect(self.returnTeoriaThirtyThree)

    # переход к экрану 'теория 35'
    def onTeoriaThirtyFiveII(self):
        self.teoria_thirty_fiveII = TeoriaThirtyFiveII()
        self.teoria_thirty_fiveII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 33' категории II
    def returnTeoriaThirtyThree(self):
        self.T34II = TeoriaThirtyThreeII()
        self.T34II.show()
        self.hide()

#экран 'теория 35' категория II
class TeoriaThirtyFiveII(QtWidgets.QMainWindow,Ui_Teoria35Window):
    def __init__(self):
        super(TeoriaThirtyFiveII, self).__init__()
        self.setupUi(self)

        self.btn_dalee35.clicked.connect(self.onTeoriaThirtySixII)
        self.btn_glavnaya35.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie35.clicked.connect(self.oglavlenieII)
        self.btn_return35.clicked.connect(self.returnTeoriaThirtyFour)

    # переход к экрану 'теория 36'
    def onTeoriaThirtySixII(self):
        self.teoria_thirty_sixII = TeoriaThirtySixII()
        self.teoria_thirty_sixII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 34' категории II
    def returnTeoriaThirtyFour(self):
        self.T35II = TeoriaThirtyFourII()
        self.T35II.show()
        self.hide()

#экран 'теория 36' категория II
class TeoriaThirtySixII(QtWidgets.QMainWindow,Ui_Teoria36Window):
    def __init__(self):
        super(TeoriaThirtySixII, self).__init__()
        self.setupUi(self)

        self.btn_dalee36.clicked.connect(self.onTeoriaThirtySevenII)
        self.btn_glavnaya36.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie36.clicked.connect(self.oglavlenieII)
        self.btn_return36.clicked.connect(self.returnTeoriaThirtyFive)

    # переход к экрану 'теория 37'
    def onTeoriaThirtySevenII(self):
        self.teoria_thirty_sevenII = TeoriaThirtySevenII()
        self.teoria_thirty_sevenII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 35' категории II
    def returnTeoriaThirtyFive(self):
        self.T36II = TeoriaThirtyFiveII()
        self.T36II.show()
        self.hide()

#экран 'теория 37' категория II
class TeoriaThirtySevenII(QtWidgets.QMainWindow,Ui_Teoria37Window):
    def __init__(self):
        super(TeoriaThirtySevenII, self).__init__()
        self.setupUi(self)

        self.btn_dalee37.clicked.connect(self.onTeoriaThirtyEightII)
        self.btn_glavnaya37.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie37.clicked.connect(self.oglavlenieII)
        self.btn_return37.clicked.connect(self.returnTeoriaThirtySix)

    # переход к экрану 'теория 38'
    def onTeoriaThirtyEightII(self):
        self.teoria_thirty_eightII = TeoriaThirtyEightII()
        self.teoria_thirty_eightII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 36' категории II
    def returnTeoriaThirtySix(self):
        self.T37II = TeoriaThirtySixII()
        self.T37II.show()
        self.hide()

#экран 'теория 38' категория II
class TeoriaThirtyEightII(QtWidgets.QMainWindow,Ui_Teoria38Window):
    def __init__(self):
        super(TeoriaThirtyEightII, self).__init__()
        self.setupUi(self)

        self.btn_dalee38.clicked.connect(self.onTeoriaThirtyNineII)
        self.btn_glavnaya38.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie38.clicked.connect(self.oglavlenieII)
        self.btn_return38.clicked.connect(self.returnTeoriaThirtySeven)

    # переход к экрану 'теория 39'
    def onTeoriaThirtyNineII(self):
        self.teoria_thirty_nineII = TeoriaThirtyNineII()
        self.teoria_thirty_nineII.show()
        self.hide()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 38' категории II
    def returnTeoriaThirtySeven(self):
        self.T38II = TeoriaThirtySevenII()
        self.T38II.show()
        self.hide()

#экран 'теория 39' категория II
class TeoriaThirtyNineII(QtWidgets.QMainWindow,Ui_Teoria39Window):
    def __init__(self):
        super(TeoriaThirtyNineII, self).__init__()
        self.setupUi(self)

        self.btn_glavnaya39.clicked.connect(self.returnGlavnayaII)
        self.btn_oglavlenie39.clicked.connect(self.oglavlenieII)
        self.btn_return39.clicked.connect(self.returnTeoriaThirtyEight)

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieII(self):
        self.oglavlenie = OglavlenieII()
        self.oglavlenie.show()

# переход к экрану 'теория 38' категории II
    def returnTeoriaThirtyEight(self):
        self.T39II = TeoriaThirtyEightII()
        self.T39II.show()
        self.hide()

#экран 'начать обучение и контроль' категории II
class TestPrompt_0II(QtWidgets.QMainWindow,Ui_TestPrompt0IIWindow):
    def __init__(self):
        super(TestPrompt_0II, self).__init__()
        self.setupUi(self)

        self.btn_begin_testprompt.clicked.connect(self.begin_testpromptII)
        self.btn_glavnaya_testprompt.clicked.connect(self.returnGlavnayaII)

    def begin_testpromptII(self):
        global numberprompt_two
        numberprompt_two = 0
        global addressprompt_two
        addressprompt_two = 0
        global resultprompt_two
        resultprompt_two = 0
        self.testPromptII = TestPromptII()
        self.testPromptII.show()
        self.close()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

#экран вопросы 'обучение и контроль'
class TestPromptII(QtWidgets.QMainWindow,Ui_TestPromptWindow):
    def __init__(self):
        super(TestPromptII, self).__init__()
        self.setupUi(self)
        self.choice_question_answers()
        #функция кнопки ДАЛЕЕ
        self.btn_dalee_testprompt.clicked.connect(self.check_answer)
        #функция кнопки НА ГЛАВНУЮ
        self.btn_glavnaya_testprompt.clicked.connect(self.returnGlavnayaII)
        #функция кнопки СПИСОК ВОПРОСОВ
        self.btn_oglavlenie_testprompt.clicked.connect(self.listquestions)

    #вернуться на 'Главную II'
    def returnGlavnayaII(self):
        self.return_glavnaya = Glavnaya_II()
        self.return_glavnaya.show()
        self.close()
    #открыть СПИСОК ВОПРОСОВ
    def listquestions(self):
        self.list_questions = QuestionsII()
        self.list_questions.show()
        self.hide()

    #функция вывода вопросов по порядку (ответы перемешиваются)
    def choice_question_answers(self):
        global addressprompt_two
        global numberprompt_two
        numberprompt_two += 1
        question = questionsII[addressprompt_two]
        answers = question_answer[question]
        answer = random.sample(answers, len(answers))
        self.textQuestion.setText(question)
        self.checkBox_1.setText(answer[0]+';')
        self.checkBox_2.setText(answer[1]+';')
        self.checkBox_3.setText(answer[2]+';')
        self.checkBox_4.setText(answer[3]+'.')
        self.labelPrompt.setText(f'Вопрос № {numberprompt_two}')
        if addressprompt_two == 0:
            # 1
            self.btn_prompt.clicked.connect(self.onTeoria1)
        elif addressprompt_two == 1:
            # 2
            self.btn_prompt.clicked.connect(self.onTeoria1)
        elif addressprompt_two == 2:
            # 3
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_two == 3:
            # 4
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_two == 4:
            # 5
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_two == 5:
            # 6
            self.btn_prompt.clicked.connect(self.onTeoria4)
        elif addressprompt_two == 6:
            # 8
            self.btn_prompt.clicked.connect(self.onTeoria6)
        elif addressprompt_two == 7:
            # 9
            self.btn_prompt.clicked.connect(self.onTeoria7)
        elif addressprompt_two == 8:
            # 10
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_two == 9:
            # 11
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_two == 10:
            # 12
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_two == 11:
            # 13
            self.btn_prompt.clicked.connect(self.onTeoria8)
        elif addressprompt_two == 12:
            # 15
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_two == 13:
            # 17
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_two == 14:
            # 18
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_two == 15:
            # 19
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_two == 16:
            # 20
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_two == 17:
            # 21
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_two == 18:
            # 22
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_two == 19:
            # 23
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_two == 20:
            # 24
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_two == 21:
            # 25
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_two == 22:
            # 27
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_two == 23:
            # 28
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_two == 24:
            # 29
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_two == 25:
            # 30
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_two == 26:
            # 31
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_two == 27:
            # 32
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_two == 28:
            # 33
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_two == 29:
            # 34
            self.btn_prompt.clicked.connect(self.onTeoria12)
        elif addressprompt_two == 30:
            # 35
            self.btn_prompt.clicked.connect(self.onTeoria12)
        elif addressprompt_two == 31:
            # 37
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_two == 32:
            # 38
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_two == 33:
            # 39
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_two == 34:
            # 40
            self.btn_prompt.clicked.connect(self.onTeoria14)
        elif addressprompt_two == 35:
            # 43
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_two == 36:
            # 44
            self.btn_prompt.clicked.connect(self.onTeoria15)
        elif addressprompt_two == 37:
            # 48
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_two == 38:
            # 51
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_two == 39:
            # 52
            self.btn_prompt.clicked.connect(self.onTeoria16)
        elif addressprompt_two == 40:
            # 54
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_two == 41:
            # 55
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_two == 42:
            # 56
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_two == 43:
            # 57
            self.btn_prompt.clicked.connect(self.onTeoria17)
        elif addressprompt_two == 44:
            # 58
            self.btn_prompt.clicked.connect(self.onTeoria18)
        elif addressprompt_two == 45:
            # 59
            self.btn_prompt.clicked.connect(self.onTeoria18)
        elif addressprompt_two == 46:
            # 60
            self.btn_prompt.clicked.connect(self.onTeoria18)
        elif addressprompt_two == 47:
            # 61
            self.btn_prompt.clicked.connect(self.onTeoria19)
        elif addressprompt_two == 48:
            # 62
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_two == 49:
            # 63
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_two == 50:
            # 64
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_two == 51:
            # 65
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_two == 52:
            # 66
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_two == 53:
            # 67
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_two == 54:
            # 68
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_two == 55:
            # 69
            self.btn_prompt.clicked.connect(self.onTeoria21)
        elif addressprompt_two == 56:
            # 70
            self.btn_prompt.clicked.connect(self.onTeoria21)
        elif addressprompt_two == 57:
            # 72
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_two == 58:
            # 73
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_two == 59:
            # 74
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_two == 60:
            # 75
            self.btn_prompt.clicked.connect(self.onTeoria22)
        elif addressprompt_two == 61:
            # 76
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_two == 62:
            # 77
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_two == 63:
            # 78
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_two == 64:
            # 79
            self.btn_prompt.clicked.connect(self.onTeoria24)
        elif addressprompt_two == 65:
            # 80
            self.btn_prompt.clicked.connect(self.onTeoria25)
        elif addressprompt_two == 66:
            # 81
            self.btn_prompt.clicked.connect(self.onTeoria25)
        elif addressprompt_two == 67:
            # 83
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 68:
            # 84
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 69:
            # 85
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 70:
            # 86
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 71:
            # 88
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 72:
            # 89
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 73:
            # 90
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 74:
            # 91
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 75:
            # 92
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 76:
            # 93
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 77:
            # 94
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_two == 78:
            # 95
            self.btn_prompt.clicked.connect(self.onTeoria27)
        elif addressprompt_two == 79:
            # 96
            self.btn_prompt.clicked.connect(self.onTeoria27)
        elif addressprompt_two == 80:
            # 97
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_two == 81:
            # 98
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_two == 82:
            # 99
            self.btn_prompt.clicked.connect(self.onTeoria28)
        elif addressprompt_two == 83:
            # 100
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_two == 84:
            # 101
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_two == 85:
            # 103
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_two == 86:
            # 104
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_two == 87:
            # 105
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_two == 88:
            # 106
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_two == 89:
            # 107
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_two == 90:
            # 108
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_two == 91:
            # 109
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_two == 92:
            # 110
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_two == 93:
            # 111
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_two == 94:
            # 112
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_two == 95:
            # 116
            self.btn_prompt.clicked.connect(self.onTeoria34)
        elif addressprompt_two == 96:
            # 117
            self.btn_prompt.clicked.connect(self.onTeoria35)
        elif addressprompt_two == 97:
            # 119
            self.btn_prompt.clicked.connect(self.onTeoria36)
        elif addressprompt_two == 98:
            # 122
            self.btn_prompt.clicked.connect(self.onTeoria37)
        elif addressprompt_two == 99:
            # 124
            self.btn_prompt.clicked.connect(self.onTeoria38)
        elif addressprompt_two == 100:
            # 125
            self.btn_prompt.clicked.connect(self.onTeoria38)
        elif addressprompt_two == 101:
            # 127
            self.btn_prompt.clicked.connect(self.onTeoria38)
        addressprompt_two += 1

    def onTeoria1(self):
        self.teoria_vp1 = TeoriaOneII()
        self.teoria_vp1.show()

    def onTeoria2(self):
        self.teoria_vp2 = TeoriaTwoII()
        self.teoria_vp2.show()

    def onTeoria3(self):
        self.teoria_vp3 = TeoriaThreeII()
        self.teoria_vp3.show()

    def onTeoria4(self):
        self.teoria_vp4 = TeoriaFourII()
        self.teoria_vp4.show()

    def onTeoria5(self):
        self.teoria_vp5 = TeoriaFiveII()
        self.teoria_vp5.show()

    def onTeoria6(self):
        self.teoria_vp6 = TeoriaSixII()
        self.teoria_vp6.show()

    def onTeoria7(self):
        self.teoria_vp7 = TeoriaSevenII()
        self.teoria_vp7.show()

    def onTeoria8(self):
        self.teoria_vp8 = TeoriaEightII()
        self.teoria_vp8.show()

    def onTeoria9(self):
        self.teoria_vp9 = TeoriaNineII()
        self.teoria_vp9.show()

    def onTeoria10(self):
        self.teoria_vp10 = TeoriaTenII()
        self.teoria_vp10.show()

    def onTeoria11(self):
        self.teoria_vp11 = TeoriaElevenII()
        self.teoria_vp11.show()

    def onTeoria12(self):
        self.teoria_vp12 = TeoriaTwelveII()
        self.teoria_vp12.show()

    def onTeoria13(self):
        self.teoria_vp13 = TeoriaThirteenII()
        self.teoria_vp13.show()

    def onTeoria14(self):
        self.teoria_vp14 = TeoriaFourteenII()
        self.teoria_vp14.show()

    def onTeoria15(self):
        self.teoria_vp15 = TeoriaFifteenII()
        self.teoria_vp15.show()

    def onTeoria16(self):
        self.teoria_vp16 = TeoriaSixteenII()
        self.teoria_vp16.show()

    def onTeoria17(self):
        self.teoria_vp17 = TeoriaSeventeenII()
        self.teoria_vp17.show()

    def onTeoria18(self):
        self.teoria_vp18 = TeoriaEighteenII()
        self.teoria_vp18.show()

    def onTeoria19(self):
        self.teoria_vp19 = TeoriaNineteenII()
        self.teoria_vp19.show()

    def onTeoria20(self):
        self.teoria_vp20 = TeoriaTwentyII()
        self.teoria_vp20.show()

    def onTeoria21(self):
        self.teoria_vp21 = TeoriaTwentyOneII()
        self.teoria_vp21.show()

    def onTeoria22(self):
        self.teoria_vp22 = TeoriaTwentyTwoII()
        self.teoria_vp22.show()

    def onTeoria23(self):
        self.teoria_vp23 = TeoriaTwentyThreeII()
        self.teoria_vp23.show()

    def onTeoria24(self):
        self.teoria_vp24 = TeoriaTwentyFourII()
        self.teoria_vp24.show()

    def onTeoria25(self):
        self.teoria_vp25 = TeoriaTwentyFiveII()
        self.teoria_vp25.show()

    def onTeoria26(self):
        self.teoria_vp26 = TeoriaTwentySixII()
        self.teoria_vp26.show()

    def onTeoria27(self):
        self.teoria_vp27 = TeoriaTwentySevenII()
        self.teoria_vp27.show()

    def onTeoria28(self):
        self.teoria_vp28 = TeoriaTwentyEightII()
        self.teoria_vp28.show()

    def onTeoria29(self):
        self.teoria_vp29 = TeoriaTwentyNineII()
        self.teoria_vp29.show()

    def onTeoria30(self):
        self.teoria_vp30 = TeoriaThirtyII()
        self.teoria_vp30.show()

    def onTeoria31(self):
        self.teoria_vp31 = TeoriaThirtyOneII()
        self.teoria_vp31.show()

    def onTeoria32(self):
        self.teoria_vp32 = TeoriaThirtyTwoII()
        self.teoria_vp32.show()

    def onTeoria33(self):
        self.teoria_vp33 = TeoriaThirtyThreeII()
        self.teoria_vp33.show()

    def onTeoria34(self):
        self.teoria_vp34 = TeoriaThirtyFourII()
        self.teoria_vp34.show()

    def onTeoria35(self):
        self.teoria_vp35 = TeoriaThirtyFiveII()
        self.teoria_vp35.show()

    def onTeoria36(self):
        self.teoria_vp36 = TeoriaThirtySixII()
        self.teoria_vp36.show()

    def onTeoria37(self):
        self.teoria_vp37 = TeoriaThirtySevenII()
        self.teoria_vp37.show()

    def onTeoria38(self):
        self.teoria_vp38 = TeoriaThirtyEightII()
        self.teoria_vp38.show()

    def onTeoria39(self):
        self.teoria_vp39 = TeoriaThirtyNineII()
        self.teoria_vp39.show()


    #очистить выбор checkbox
    def clear(self):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)

    #подсчет правильных ответов
    def check_answer(self):
        if self.checkBox_1.text() in correct_answer and self.checkBox_2.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_1.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_1.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_2.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_2.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_3.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_1.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_2.text() in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_3.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_4.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_1.text() not in correct_answer:
            if self.checkBox_4.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_1.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()


    #вывод экрана при нажатии ДАЛЕЕ
    def quantity_question(self):
        if numberprompt_two < 102:
            self.choice_question_answers()
        elif numberprompt_two == 102:
            self.resultatWindowII()

    #экран 'Результат'
    def resultatWindowII(self):
        self.RWindow = ResultatPromptII()
        self.RWindow.show()
        self.close()
    # диалоговое окно ВЕРНО
    def right(self):
        self.onRight = Right()
        self.onRight.show()
    # диалоговое окно НЕВЕРНО
    def wrong(self):
        self.onWrong = Wrong()
        self.onWrong.show()

#окно 'Результат' режима 'Обучение и контроль' категории II
class ResultatPromptII(QtWidgets.QMainWindow,Ui_ResultatPromWindow):
    def __init__(self):
        super(ResultatPromptII, self).__init__()
        self.setupUi(self)

        self.btn_glavnaya.clicked.connect(self.returnGlavnayaII)
        self.btn_again.clicked.connect(self.onAgainPrompt)

    def onAgainPrompt(self):
        self.on_again =TestPrompt_0II()
        self.on_again.show()
        self.close()

    def returnGlavnayaII(self):
        self.return_glavnayaII = Glavnaya_II()
        self.return_glavnayaII.show()
        self.close()

#экран 'начать контрольный тест'категории II
class Test_0II(QtWidgets.QMainWindow,Ui_Test0Window):
    def __init__(self):
        super(Test_0II, self).__init__()
        self.setupUi(self)

        self.btn_begin_test.clicked.connect(self.begin_test)
        self.btn_glavnaya_test.clicked.connect(self.returnGlavnayaII)

    def begin_test(self):
        global number_two
        number_two = 0
        global result_two
        result_two = 0
        self.test_2 = TestII()
        self.test_2.show()
        self.close()

# переход к экрану 'главная II'
    def returnGlavnayaII(self):
        self.GII = Glavnaya_II()
        self.GII.show()
        self.close()

#экран вопросы 'контрольный тест' категории II
class TestII(QtWidgets.QMainWindow,Ui_TestWindow):
    def __init__(self):
        super(TestII, self).__init__()
        self.setupUi(self)
        self.choice_question_answers()

        self.btn_dalee_test.clicked.connect(self.check_answer)
        self.btn_glavnaya_test.clicked.connect(self.returnGlavnaya)

    def returnGlavnaya(self):
        self.return_glavnaya = Glavnaya_II()
        self.return_glavnaya.show()
        self.close()

    def clear(self):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)

    def choice_question_answers(self):
        question = random.choice(questionsII)
        answers = question_answer[question]
        answer = random.sample(answers, len(answers))
        self.textQuestion.setText(question)
        self.checkBox_1.setText(answer[0]+';')
        self.checkBox_2.setText(answer[1]+';')
        self.checkBox_3.setText(answer[2]+';')
        self.checkBox_4.setText(answer[3]+';')
        global number_two
        number_two = number_two+1
        self.label.setText(f'Вопрос № {number_two}')

    def check_answer(self):
        global result_two
        if self.checkBox_1.text() in correct_answer and self.checkBox_2.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() == True:
                result_two +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True:
                result_two +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_2.isChecked() == True:
                result_two +=0.5
            else:
                result_two +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() == True:
                result_two +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() != True:
                result_two +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() == True:
                result_two +=0.5
            else:
                result_two +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_two +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_two +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_two +=0.5
            else:
                result_two +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() == True:
                result_two +=1
            elif self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() != True:
                result_two +=0.5
            elif self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() == True:
                result_two +=0.5
            else:
                result_two +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_two +=1
            elif self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_two +=0.5
            elif self.checkBox_2.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_two +=0.5
            else:
                result_two +=0
        elif self.checkBox_3.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_two +=1
            elif self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_two +=0.5
            elif self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_two +=0.5
            else:
                result_two +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_two +=1
            else:
                result_two +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_two +=1
            else:
                result_two +=0
        elif self.checkBox_3.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_two +=1
            else:
                result_two +=0
        elif self.checkBox_4.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_1.text() not in correct_answer:
            if self.checkBox_4.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_1.isChecked() != True:
                result_two +=1
            else:
                result_two +=0

        self.clear()
        self.quantity_question()

    def quantity_question(self):
        if number_two < 20:
            self.choice_question_answers()
        elif number_two == 20:
            self.resultatWindowII()

    def resultatWindowII(self):
        self.RWindow = ResultatII()
        self.RWindow.show()
        self.close()

#экран 'результат контрольного теста' категория II
class ResultatII(QtWidgets.QMainWindow,Ui_ResultatWindow):
    def __init__(self):
        super(ResultatII, self).__init__()
        self.setupUi(self)
        self.result.setText(str(result_two) + ' из 20.0')


        self.btn_glavnaya.clicked.connect(self.returnGlavnayaII)
        self.btn_again.clicked.connect(self.onAgain)

    def onAgain(self):
        self.on_again = Test_0II()
        self.on_again.show()
        self.close()

    def returnGlavnayaII(self):
        self.return_glavnayaII = Glavnaya_II()
        self.return_glavnayaII.show()
        self.close()

#теория 1 категории III
class TeoriaOneIII(QtWidgets.QMainWindow,Ui_Teoria1Window):
    def __init__(self):
        super(TeoriaOneIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee1.clicked.connect(self.onTeoriaTwo)
        self.btn_oglavlenie1.clicked.connect(self.oglavlenieIII)
        self.btn_glavnaya1.clicked.connect(self.returnGlavnayaIII)

#переход к экрану 'теория 2' категории III
    def onTeoriaTwo(self):
        self.teoria_two = TeoriaTwoIII()
        self.teoria_two.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie_1 = OglavlenieIII()
        self.oglavlenie_1.show()

# переход к главному экрану 'теория 2' категории III
    def returnGlavnayaIII(self):
        self.GI = Glavnaya_III()
        self.GI.show()
        self.close()

#экран 'теория 2' категория III
class TeoriaTwoIII(QtWidgets.QMainWindow,Ui_Teoria2Window):
    def __init__(self):
        super(TeoriaTwoIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee2.clicked.connect(self.onTeoriaThree)
        self.btn_glavnaya2.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie2.clicked.connect(self.oglavlenieIII)
        self.btn_return2.clicked.connect(self.returnTeoriaOne)

#переход к экрану 'теория 3' категории III
    def onTeoriaThree(self):
        self.teoria_three = TeoriaThreeIII()
        self.teoria_three.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie_ = OglavlenieIII()
        self.oglavlenie_.show()

#переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к главному экрану 'теория 1' категории III
    def returnTeoriaOne(self):
        self.T1I = TeoriaOneIII()
        self.T1I.show()
        self.hide()

#экран 'теория 3' категории III
class TeoriaThreeIII(QtWidgets.QMainWindow,Ui_Teoria3Window):
    def __init__(self):
        super(TeoriaThreeIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee3.clicked.connect(self.onTeoriaFour)
        self.btn_glavnaya3.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie3.clicked.connect(self.oglavlenieIII)
        self.btn_return3.clicked.connect(self.returnTeoriaTwo)

#переход к экрану 'теория 4' категории III
    def onTeoriaFour(self):
        self.teoria_four = TeoriaFourIII()
        self.teoria_four.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie_ = OglavlenieIII()
        self.oglavlenie_.show()

# переход к экрану 'главная I'
    def returnGlavnayaIII(self):
        self.GI = Glavnaya_III()
        self.GI.show()
        self.close()

# переход к экрану 'теория 2' категории III
    def returnTeoriaTwo(self):
        self.T2I = TeoriaTwoIII()
        self.T2I.show()
        self.hide()

#экран 'теория 4' категории III
class TeoriaFourIII(QtWidgets.QMainWindow,Ui_Teoria4Window):
    def __init__(self):
        super(TeoriaFourIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee4.clicked.connect(self.onTeoriaFive)
        self.btn_glavnaya4.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie4.clicked.connect(self.oglavlenieIII)
        self.btn_return4.clicked.connect(self.returnTeoriaThree)

# переход к экрану 'теория 5'
    def onTeoriaFive(self):
        self.teoria_five = TeoriaFiveIII()
        self.teoria_five.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

#переход к экрану 'главная I'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 3' категории I
    def returnTeoriaThree(self):
        self.T3III = TeoriaThreeIII()
        self.T3III.show()
        self.hide()

#экран 'теория 5' категории III
class TeoriaFiveIII(QtWidgets.QMainWindow,Ui_Teoria5Window):
    def __init__(self):
        super(TeoriaFiveIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee5.clicked.connect(self.onTeoriaSix)
        self.btn_glavnaya5.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie5.clicked.connect(self.oglavlenieIII)
        self.btn_return5.clicked.connect(self.returnTeoriaFour)

#переход к экрану 'теория 6'
    def onTeoriaSix(self):
        self.teoria_six = TeoriaSixIII()
        self.teoria_six.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

#переход к экрану 'главная I'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 4' категории III
    def returnTeoriaFour(self):
        self.T4III = TeoriaFourIII()
        self.T4III.show()
        self.hide()

#экран 'теория 6' категории III
class TeoriaSixIII(QtWidgets.QMainWindow,Ui_Teoria6Window):
    def __init__(self):
        super(TeoriaSixIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee6.clicked.connect(self.onTeoriaSeven)
        self.btn_glavnaya6.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie6.clicked.connect(self.oglavlenieIII)
        self.btn_return6.clicked.connect(self.returnTeoriaFive)

# переход к экрану 'теория 7'
    def onTeoriaSeven(self):
        self.teoria_seven = TeoriaSevenIII()
        self.teoria_seven.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная I'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 5' категории III
    def returnTeoriaFive(self):
        self.T5III = TeoriaFiveIII()
        self.T5III.show()
        self.hide()

#экран 'теория 7' категории III
class TeoriaSevenIII(QtWidgets.QMainWindow,Ui_Teoria7Window):
    def __init__(self):
        super(TeoriaSevenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee7.clicked.connect(self.onTeoriaEight)
        self.btn_glavnaya7.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie7.clicked.connect(self.oglavlenieIII)
        self.btn_return7.clicked.connect(self.returnTeoriaSix)

# переход к экрану 'теория 8'
    def onTeoriaEight(self):
        self.teoria_eight = TeoriaEightIII()
        self.teoria_eight.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 6' категории III
    def returnTeoriaSix(self):
        self.T6III = TeoriaSixIII()
        self.T6III.show()
        self.hide()

#экран 'теория 8' категории III
class TeoriaEightIII(QtWidgets.QMainWindow,Ui_Teoria8Window):
    def __init__(self):
        super(TeoriaEightIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee8.clicked.connect(self.onTeoriaNine)
        self.btn_glavnaya8.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie8.clicked.connect(self.oglavlenieIII)
        self.btn_return8.clicked.connect(self.returnTeoriaSeven)

# переход к экрану 'теория 9'
    def onTeoriaNine(self):
        self.teoria_nine = TeoriaNineIII()
        self.teoria_nine.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 7' категории III
    def returnTeoriaSeven(self):
        self.T7III = TeoriaSevenIII()
        self.T7III.show()
        self.hide()

#экран 'теория 9' категории III
class TeoriaNineIII(QtWidgets.QMainWindow,Ui_Teoria9Window):
    def __init__(self):
        super(TeoriaNineIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee9.clicked.connect(self.onTeoriaTen)
        self.btn_glavnaya9.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie9.clicked.connect(self.oglavlenieIII)
        self.btn_return9.clicked.connect(self.returnTeoriaEight)

# переход к экрану 'теория 10'
    def onTeoriaTen(self):
        self.teoria_ten = TeoriaTenIII()
        self.teoria_ten.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 8' категории III
    def returnTeoriaEight(self):
        self.T8III = TeoriaEightIII()
        self.T8III.show()
        self.hide()

#экран 'теория 10' категории III
class TeoriaTenIII(QtWidgets.QMainWindow,Ui_Teoria10Window):
    def __init__(self):
        super(TeoriaTenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee10.clicked.connect(self.onTeoriaEleven)
        self.btn_glavnaya10.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie10.clicked.connect(self.oglavlenieIII)
        self.btn_return10.clicked.connect(self.returnTeoriaNine)

# переход к экрану 'теория 11'
    def onTeoriaEleven(self):
        self.teoria_eleven = TeoriaElevenIII()
        self.teoria_eleven.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 9' категории III
    def returnTeoriaNine(self):
        self.T9III = TeoriaNineIII()
        self.T9III.show()
        self.hide()

#экран 'теория 11' категории III
class TeoriaElevenIII(QtWidgets.QMainWindow,Ui_Teoria11Window):
    def __init__(self):
        super(TeoriaElevenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee11.clicked.connect(self.onTeoriaTwelve)
        self.btn_glavnaya11.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie11.clicked.connect(self.oglavlenieIII)
        self.btn_return11.clicked.connect(self.returnTeoriaTen)

# переход к экрану 'теория 12'
    def onTeoriaTwelve(self):
        self.teoria_twelve = TeoriaTwelveIII()
        self.teoria_twelve.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 10' категории III
    def returnTeoriaTen(self):
        self.T10III = TeoriaTenIII()
        self.T10III.show()
        self.hide()

#экран 'теория 12' категории III
class TeoriaTwelveIII(QtWidgets.QMainWindow,Ui_Teoria12Window):
    def __init__(self):
        super(TeoriaTwelveIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee12.clicked.connect(self.onTeoriaThirteen)
        self.btn_glavnaya12.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie12.clicked.connect(self.oglavlenieIII)
        self.btn_return12.clicked.connect(self.returnTeoriaEleven)

# переход к экрану 'теория 13'
    def onTeoriaThirteen(self):
        self.teoria_thirteen = TeoriaThirteenIII()
        self.teoria_thirteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 11' категории III
    def returnTeoriaEleven(self):
        self.T11III = TeoriaElevenIII()
        self.T11III.show()
        self.hide()

#экран 'теория 13' категории III
class TeoriaThirteenIII(QtWidgets.QMainWindow,Ui_Teoria13Window):
    def __init__(self):
        super(TeoriaThirteenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee13.clicked.connect(self.onTeoriaFourteen)
        self.btn_glavnaya13.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie13.clicked.connect(self.oglavlenieIII)
        self.btn_return13.clicked.connect(self.returnTeoriaTwelve)

# переход к экрану 'теория 14'
    def onTeoriaFourteen(self):
        self.teoria_fourteen = TeoriaFourteenIII()
        self.teoria_fourteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 12' категории III
    def returnTeoriaTwelve(self):
        self.T12III = TeoriaTwelveIII()
        self.T12III.show()
        self.hide()

#экран 'теория 14' категории III
class TeoriaFourteenIII(QtWidgets.QMainWindow,Ui_Teoria14Window):
    def __init__(self):
        super(TeoriaFourteenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee14.clicked.connect(self.onTeoriaFifteen)
        self.btn_glavnaya14.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie14.clicked.connect(self.oglavlenieIII)
        self.btn_return14.clicked.connect(self.returnTeoriaThirteen)

# переход к экрану 'теория 15'
    def onTeoriaFifteen(self):
        self.teoria_fifteen = TeoriaFifteenIII()
        self.teoria_fifteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 13' категории III
    def returnTeoriaThirteen(self):
        self.T13III = TeoriaThirteenIII()
        self.T13III.show()
        self.hide()

#экран 'теория 15' категории III
class TeoriaFifteenIII(QtWidgets.QMainWindow,Ui_Teoria15Window):
    def __init__(self):
        super(TeoriaFifteenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee15.clicked.connect(self.onTeoriaSixteen)
        self.btn_glavnaya15.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie15.clicked.connect(self.oglavlenieIII)
        self.btn_return15.clicked.connect(self.returnTeoriaFourteen)

# переход к экрану 'теория 16'
    def onTeoriaSixteen(self):
        self.teoria_sixteen = TeoriaSixteenIII()
        self.teoria_sixteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 14' категории III
    def returnTeoriaFourteen(self):
        self.T14III = TeoriaFourteenIII()
        self.T14III.show()
        self.hide()

#экран 'теория 16' категории III
class TeoriaSixteenIII(QtWidgets.QMainWindow,Ui_Teoria16Window):
    def __init__(self):
        super(TeoriaSixteenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee16.clicked.connect(self.onTeoriaSeventeen)
        self.btn_glavnaya16.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie16.clicked.connect(self.oglavlenieIII)
        self.btn_return16.clicked.connect(self.returnTeoriaFifteen)

# переход к экрану 'теория 17'
    def onTeoriaSeventeen(self):
        self.teoria_seventeen = TeoriaSeventeenIII()
        self.teoria_seventeen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 15' категории III
    def returnTeoriaFifteen(self):
        self.T15III = TeoriaFifteenIII()
        self.T15III.show()
        self.hide()

#экран 'теория 17' категории III
class TeoriaSeventeenIII(QtWidgets.QMainWindow,Ui_Teoria17Window):
    def __init__(self):
        super(TeoriaSeventeenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee17.clicked.connect(self.onTeoriaEighteen)
        self.btn_glavnaya17.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie17.clicked.connect(self.oglavlenieIII)
        self.btn_return17.clicked.connect(self.returnTeoriaSixteen)

# переход к экрану 'теория 18'
    def onTeoriaEighteen(self):
        self.teoria_eighteen = TeoriaEighteenIII()
        self.teoria_eighteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 16' категории I
    def returnTeoriaSixteen(self):
        self.T16III = TeoriaSixteenIII()
        self.T16III.show()
        self.hide()

#экран 'теория 18' категории III
class TeoriaEighteenIII(QtWidgets.QMainWindow,Ui_Teoria18Window):
    def __init__(self):
        super(TeoriaEighteenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee18.clicked.connect(self.onTeoriaNineteen)
        self.btn_glavnaya18.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie18.clicked.connect(self.oglavlenieIII)
        self.btn_return18.clicked.connect(self.returnTeoriaSeventeen)

# переход к экрану 'теория 19'
    def onTeoriaNineteen(self):
        self.teoria_nineteen = TeoriaNineteenIII()
        self.teoria_nineteen.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 17' категории III
    def returnTeoriaSeventeen(self):
        self.T17III = TeoriaSeventeenIII()
        self.T17III.show()
        self.hide()

#экран 'теория 19' категории III
class TeoriaNineteenIII(QtWidgets.QMainWindow,Ui_Teoria19Window):
    def __init__(self):
        super(TeoriaNineteenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee19.clicked.connect(self.onTeoriaTwenty)
        self.btn_glavnaya19.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie19.clicked.connect(self.oglavlenieIII)
        self.btn_return19.clicked.connect(self. returnTeoriaEighteen)

# переход к экрану 'теория 20'
    def onTeoriaTwenty(self):
        self.teoria_twenty = TeoriaTwentyIII()
        self.teoria_twenty.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 18' категории III
    def returnTeoriaEighteen(self):
        self.T18III = TeoriaEighteenIII()
        self.T18III.show()
        self.hide()

#экран 'теория 20' категории III
class TeoriaTwentyIII(QtWidgets.QMainWindow,Ui_Teoria20Window):
    def __init__(self):
        super(TeoriaTwentyIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee20.clicked.connect(self.onTeoriaTwentyOne)
        self.btn_glavnaya20.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie20.clicked.connect(self.oglavlenieIII)
        self.btn_return20.clicked.connect(self.returnTeoriaNineteen)

# переход к экрану 'теория 21'
    def onTeoriaTwentyOne(self):
        self.teoria_twenty_one = TeoriaTwentyOneIII()
        self.teoria_twenty_one.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 19' категории I
    def returnTeoriaNineteen(self):
        self.T19III = TeoriaNineteenIII()
        self.T19III.show()
        self.hide()

#экран 'теория 21' категории III
class TeoriaTwentyOneIII(QtWidgets.QMainWindow,Ui_Teoria21Window):
    def __init__(self):
        super(TeoriaTwentyOneIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee21.clicked.connect(self.onTeoriaTwentyTwo)
        self.btn_glavnaya21.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie21.clicked.connect(self.oglavlenieIII)
        self.btn_return21.clicked.connect(self.returnTeoriaTwenty)

# переход к экрану 'теория 22'
    def onTeoriaTwentyTwo(self):
        self.teoria_twenty_two = TeoriaTwentyTwoIII()
        self.teoria_twenty_two.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 20' категории III
    def returnTeoriaTwenty(self):
        self.T20III = TeoriaTwentyIII()
        self.T20III.show()
        self.hide()

#экран 'теория 22' категории III
class TeoriaTwentyTwoIII(QtWidgets.QMainWindow,Ui_Teoria22Window):
    def __init__(self):
        super(TeoriaTwentyTwoIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee22.clicked.connect(self.onTeoriaTwentyThree)
        self.btn_glavnaya22.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie22.clicked.connect(self.oglavlenieIII)
        self.btn_return22.clicked.connect(self.returnTeoriaTwentyOne)

# переход к экрану 'теория 23'
    def onTeoriaTwentyThree(self):
        self.teoria_twenty_three = TeoriaTwentyThreeIII()
        self.teoria_twenty_three.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 21' категории III
    def returnTeoriaTwentyOne(self):
        self.T21III = TeoriaTwentyOneIII()
        self.T21III.show()
        self.hide()

#экран 'теория 23' категории III
class TeoriaTwentyThreeIII(QtWidgets.QMainWindow,Ui_Teoria23Window):
    def __init__(self):
        super(TeoriaTwentyThreeIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee23.clicked.connect(self.onTeoriaTwentyFour)
        self.btn_glavnaya23.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie23.clicked.connect(self.oglavlenieIII)
        self.btn_return23.clicked.connect(self.returnTeoriaTwentyTwo)

# переход к экрану 'теория 24'
    def onTeoriaTwentyFour(self):
        self.teoria_twenty_four = TeoriaTwentyFourIII()
        self.teoria_twenty_four.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 22' категории III
    def returnTeoriaTwentyTwo(self):
        self.T22III = TeoriaTwentyTwoIII()
        self.T22III.show()
        self.hide()

#экран 'теория 24' категории III
class TeoriaTwentyFourIII(QtWidgets.QMainWindow,Ui_Teoria24Window):
    def __init__(self):
        super(TeoriaTwentyFourIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee24.clicked.connect(self.onTeoriaTwentyFive)
        self.btn_glavnaya24.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie24.clicked.connect(self.oglavlenieIII)
        self.btn_return24.clicked.connect(self.returnTeoriaTwentyThree)

# переход к экрану 'теория 25'
    def onTeoriaTwentyFive(self):
        self.teoria_twenty_five = TeoriaTwentyFiveIII()
        self.teoria_twenty_five.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 23' категории III
    def returnTeoriaTwentyThree(self):
        self.T23III = TeoriaTwentyThreeIII()
        self.T23III.show()
        self.hide()

#экран 'теория 25' категории III
class TeoriaTwentyFiveIII(QtWidgets.QMainWindow,Ui_Teoria25Window):
    def __init__(self):
        super(TeoriaTwentyFiveIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee25.clicked.connect(self.onTeoriaTwentySix)
        self.btn_glavnaya25.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie25.clicked.connect(self.oglavlenieIII)
        self.btn_return25.clicked.connect(self.returnTeoriaTwentyFour)

# переход к экрану 'теория 26'
    def onTeoriaTwentySix(self):
        self.teoria_twenty_six = TeoriaTwentySixIII()
        self.teoria_twenty_six.show()
        self.hide()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'теория 24' категории III
    def returnTeoriaTwentyFour(self):
        self.T24III = TeoriaTwentyFourIII()
        self.T24III.show()
        self.hide()

#экран 'теория 26' категории III
class TeoriaTwentySixIII(QtWidgets.QMainWindow,Ui_Teoria26Window):
    def __init__(self):
        super(TeoriaTwentySixIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee26.clicked.connect(self.onTeoriaTwentySeven)
        self.btn_glavnaya26.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie26.clicked.connect(self.oglavlenieIII)
        self.btn_return26.clicked.connect(self.returnTeoriaTwentyFive)

# переход к экрану 'теория 27'
    def onTeoriaTwentySeven(self):
        self.teoria_twenty_seven = TeoriaTwentySevenIII()
        self.teoria_twenty_seven.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 25' категории III
    def returnTeoriaTwentyFive(self):
        self.T25III = TeoriaTwentyFiveIII()
        self.T25III.show()
        self.hide()

#экран 'теория 27' категории III
class TeoriaTwentySevenIII(QtWidgets.QMainWindow,Ui_Teoria27Window):
    def __init__(self):
        super(TeoriaTwentySevenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee27.clicked.connect(self.onTeoriaTwentyEight)
        self.btn_glavnaya27.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie27.clicked.connect(self.oglavlenieIII)
        self.btn_return27.clicked.connect(self.returnTeoriaTwentySix)

    # переход к экрану 'теория 28'
    def onTeoriaTwentyEight(self):
        self.teoria_twenty_eight = TeoriaTwentyEightIII()
        self.teoria_twenty_eight.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 26' категории III
    def returnTeoriaTwentySix(self):
        self.T26III = TeoriaTwentySixIII()
        self.T26III.show()
        self.hide()

#экран 'теория 28' категории III
class TeoriaTwentyEightIII(QtWidgets.QMainWindow,Ui_Teoria28Window):
    def __init__(self):
        super(TeoriaTwentyEightIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee28.clicked.connect(self.onTeoriaTwentyNine)
        self.btn_glavnaya28.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie28.clicked.connect(self.oglavlenieIII)
        self.btn_return28.clicked.connect(self.returnTeoriaTwentySeven)

    # переход к экрану 'теория 29'
    def onTeoriaTwentyNine(self):
        self.teoria_twenty_nine = TeoriaTwentyNineIII()
        self.teoria_twenty_nine.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie_ = OglavlenieIII()
        self.oglavlenie_.show()

# переход к экрану 'теория 27' категории III
    def returnTeoriaTwentySeven(self):
        self.T27III = TeoriaTwentySevenIII()
        self.T27III.show()
        self.hide()

#экран 'теория 29' категория III
class TeoriaTwentyNineIII(QtWidgets.QMainWindow,Ui_Teoria29Window):
    def __init__(self):
        super(TeoriaTwentyNineIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee29.clicked.connect(self.onTeoriaThirty)
        self.btn_glavnaya29.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie29.clicked.connect(self.oglavlenieIII)
        self.btn_return29.clicked.connect(self.returnTeoriaTwentyEight)

    # переход к экрану 'теория 30'
    def onTeoriaThirty(self):
        self.teoria_thirty = TeoriaThirtyIII()
        self.teoria_thirty.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 28' категории III
    def returnTeoriaTwentyEight(self):
        self.T29III = TeoriaTwentyEightIII()
        self.T29III.show()
        self.hide()

#экран 'теория 30' категория III
class TeoriaThirtyIII(QtWidgets.QMainWindow,Ui_Teoria30Window):
    def __init__(self):
        super(TeoriaThirtyIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee30.clicked.connect(self.onTeoriaThirtyOne)
        self.btn_glavnaya30.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie30.clicked.connect(self.oglavlenieIII)
        self.btn_return30.clicked.connect(self.returnTeoriaTwentyNine)

    # переход к экрану 'теория 31'
    def onTeoriaThirtyOne(self):
        self.teoria_thirty_one = TeoriaThirtyOneIII()
        self.teoria_thirty_one.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 29' категории III
    def returnTeoriaTwentyNine(self):
        self.T30III = TeoriaTwentyNineIII()
        self.T30III.show()
        self.hide()

#экран 'теория 31' категория III
class TeoriaThirtyOneIII(QtWidgets.QMainWindow,Ui_Teoria31Window):
    def __init__(self):
        super(TeoriaThirtyOneIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee31.clicked.connect(self.onTeoriaThirtyTwo)
        self.btn_glavnaya31.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie31.clicked.connect(self.oglavlenieIII)
        self.btn_return31.clicked.connect(self.returnTeoriaThirty)

    # переход к экрану 'теория 32'
    def onTeoriaThirtyTwo(self):
        self.teoria_thirty_two = TeoriaThirtyTwoIII()
        self.teoria_thirty_two.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie_ = OglavlenieIII()
        self.oglavlenie_.show()

# переход к экрану 'теория 30' категории III
    def returnTeoriaThirty(self):
        self.T31III = TeoriaThirtyIII()
        self.T31III.show()
        self.hide()

#экран 'теория 32' категория III
class TeoriaThirtyTwoIII(QtWidgets.QMainWindow,Ui_Teoria32Window):
    def __init__(self):
        super(TeoriaThirtyTwoIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee32.clicked.connect(self.onTeoriaThirtyThree)
        self.btn_glavnaya32.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie32.clicked.connect(self.oglavlenieIII)
        self.btn_return32.clicked.connect(self.returnTeoriaThirtyOne)

    # переход к экрану 'теория 33'
    def onTeoriaThirtyThree(self):
        self.teoria_thirty_three = TeoriaThirtyThreeIII()
        self.teoria_thirty_three.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 31' категории III
    def returnTeoriaThirtyOne(self):
        self.T32III = TeoriaThirtyOneIII()
        self.T32III.show()
        self.hide()

#экран 'теория 33' категория III
class TeoriaThirtyThreeIII(QtWidgets.QMainWindow,Ui_Teoria33Window):
    def __init__(self):
        super(TeoriaThirtyThreeIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee33.clicked.connect(self.onTeoriaThirtyFour)
        self.btn_glavnaya33.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie33.clicked.connect(self.oglavlenieIII)
        self.btn_return33.clicked.connect(self.returnTeoriaThirtyTwo)

    # переход к экрану 'теория 34'
    def onTeoriaThirtyFour(self):
        self.teoria_thirty_four = TeoriaThirtyFourIII()
        self.teoria_thirty_four.show()
        self.hide()


# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 32' категории III
    def returnTeoriaThirtyTwo(self):
        self.T33III = TeoriaThirtyTwoIII()
        self.T33III.show()
        self.hide()

#экран 'теория 34' категория III
class TeoriaThirtyFourIII(QtWidgets.QMainWindow,Ui_Teoria34Window):
    def __init__(self):
        super(TeoriaThirtyFourIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee34.clicked.connect(self.onTeoriaThirtyFive)
        self.btn_glavnaya34.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie34.clicked.connect(self.oglavlenieIII)
        self.btn_return34.clicked.connect(self.returnTeoriaThirtyThree)

    # переход к экрану 'теория 35'
    def onTeoriaThirtyFive(self):
        self.teoria_thirty_five = TeoriaThirtyFiveIII()
        self.teoria_thirty_five.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 33' категории III
    def returnTeoriaThirtyThree(self):
        self.T34III = TeoriaThirtyThreeIII()
        self.T34III.show()
        self.hide()

#экран 'теория 35' категория III
class TeoriaThirtyFiveIII(QtWidgets.QMainWindow,Ui_Teoria35Window):
    def __init__(self):
        super(TeoriaThirtyFiveIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee35.clicked.connect(self.onTeoriaThirtySix)
        self.btn_glavnaya35.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie35.clicked.connect(self.oglavlenieIII)
        self.btn_return35.clicked.connect(self.returnTeoriaThirtyFour)

    # переход к экрану 'теория 36'
    def onTeoriaThirtySix(self):
        self.teoria_thirty_six = TeoriaThirtySixIII()
        self.teoria_thirty_six.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 34' категории III
    def returnTeoriaThirtyFour(self):
        self.T35III = TeoriaThirtyFourIII()
        self.T35III.show()
        self.hide()

#экран 'теория 36' категория III
class TeoriaThirtySixIII(QtWidgets.QMainWindow,Ui_Teoria36Window):
    def __init__(self):
        super(TeoriaThirtySixIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee36.clicked.connect(self.onTeoriaThirtySeven)
        self.btn_glavnaya36.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie36.clicked.connect(self.oglavlenieIII)
        self.btn_return36.clicked.connect(self.returnTeoriaThirtyFive)

    # переход к экрану 'теория 37'
    def onTeoriaThirtySeven(self):
        self.teoria_thirty_seven = TeoriaThirtySevenIII()
        self.teoria_thirty_seven.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 35' категории III
    def returnTeoriaThirtyFive(self):
        self.T36III = TeoriaThirtyFiveIII()
        self.T36III.show()
        self.hide()

#экран 'теория 37' категория III
class TeoriaThirtySevenIII(QtWidgets.QMainWindow,Ui_Teoria37Window):
    def __init__(self):
        super(TeoriaThirtySevenIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee37.clicked.connect(self.onTeoriaThirtyEight)
        self.btn_glavnaya37.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie37.clicked.connect(self.oglavlenieIII)
        self.btn_return37.clicked.connect(self.returnTeoriaThirtySix)

    # переход к экрану 'теория 38'
    def onTeoriaThirtyEight(self):
        self.teoria_thirty_eight = TeoriaThirtyEightIII()
        self.teoria_thirty_eight.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 36' категории III
    def returnTeoriaThirtySix(self):
        self.T37III = TeoriaThirtySixIII()
        self.T37III.show()
        self.hide()

#экран 'теория 38' категория III
class TeoriaThirtyEightIII(QtWidgets.QMainWindow,Ui_Teoria38Window):
    def __init__(self):
        super(TeoriaThirtyEightIII, self).__init__()
        self.setupUi(self)

        self.btn_dalee38.clicked.connect(self.onTeoriaThirtyNine)
        self.btn_glavnaya38.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie38.clicked.connect(self.oglavlenieIII)
        self.btn_return38.clicked.connect(self.returnTeoriaThirtySeven)

    # переход к экрану 'теория 39'
    def onTeoriaThirtyNine(self):
        self.teoria_thirty_nine = TeoriaThirtyNineIII()
        self.teoria_thirty_nine.show()
        self.hide()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenie = OglavlenieIII()
        self.oglavlenie.show()

# переход к экрану 'теория 38' категории III
    def returnTeoriaThirtySeven(self):
        self.T38III = TeoriaThirtySevenIII()
        self.T38III.show()
        self.hide()

#экран 'теория 39' категория III
class TeoriaThirtyNineIII(QtWidgets.QMainWindow,Ui_Teoria39Window):
    def __init__(self):
        super(TeoriaThirtyNineIII, self).__init__()
        self.setupUi(self)

        self.btn_glavnaya39.clicked.connect(self.returnGlavnayaIII)
        self.btn_oglavlenie39.clicked.connect(self.oglavlenieIII)
        self.btn_return39.clicked.connect(self.returnTeoriaThirtyEight)

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

# переход к экрану 'оглавление'
    def oglavlenieIII(self):
        self.oglavlenieIII = OglavlenieIII()
        self.oglavlenieIII.show()

# переход к экрану 'теория 38' категории III
    def returnTeoriaThirtyEight(self):
        self.T39III = TeoriaThirtyEightIII()
        self.T39III.show()
        self.hide()

#экран 'начать обучение и контроль' категории III
class TestPrompt_0III(QtWidgets.QMainWindow,Ui_TestPrompt0IIIWindow):
    def __init__(self):
        super(TestPrompt_0III, self).__init__()
        self.setupUi(self)
        self.btn_begin_testprompt.clicked.connect(self.begin_testpromptIII)
        self.btn_glavnaya_testprompt.clicked.connect(self.returnGlavnayaIII)

    def begin_testpromptIII(self):
        global numberprompt_three
        numberprompt_three = 0
        global addressprompt_three
        addressprompt_three = 0
        global resultprompt_three
        resultprompt_three = 0
        self.testPromptIII = TestPromptIII()
        self.testPromptIII.show()
        self.close()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

#экран вопросы 'обучение и контроль' категории III
class TestPromptIII(QtWidgets.QMainWindow,Ui_TestPromptWindow):
    def __init__(self):
        super(TestPromptIII, self).__init__()
        self.setupUi(self)
        self.choice_question_answers()
        #функция кнопки ДАЛЕЕ
        self.btn_dalee_testprompt.clicked.connect(self.check_answer)
        #функция кнопки НА ГЛАВНУЮ
        self.btn_glavnaya_testprompt.clicked.connect(self.returnGlavnayaIII)
        # функция кнопки СПИСОК ВОПРОСОВ
        self.btn_oglavlenie_testprompt.clicked.connect(self.listquestions)

    #вернуться на 'Главную III'
    def returnGlavnayaIII(self):
        self.return_glavnaya = Glavnaya_III()
        self.return_glavnaya.show()
        self.close()
    #открыть СПИСОК ВОПРОСОВ
    def listquestions(self):
        self.list_questions = QuestionsIII()
        self.list_questions.show()
        self.hide()

    #функция вывода вопросов по порядку (ответы перемешиваются)
    def choice_question_answers(self):
        global addressprompt_three
        global numberprompt_three
        numberprompt_three += 1
        question = questionsIII[addressprompt_three]
        answers = question_answer[question]
        answer = random.sample(answers, len(answers))
        self.textQuestion.setText(question)
        self.checkBox_1.setText(answer[0] + ';')
        self.checkBox_2.setText(answer[1] + ';')
        self.checkBox_3.setText(answer[2] + ';')
        self.checkBox_4.setText(answer[3] + '.')
        self.labelPrompt.setText(f'Вопрос № {numberprompt_three}')
        if addressprompt_three == 0:
            # 1
            self.btn_prompt.clicked.connect(self.onTeoria1)
        elif addressprompt_three == 1:
            # 3
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_three == 2:
            # 4
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_three == 3:
            # 5
            self.btn_prompt.clicked.connect(self.onTeoria3)
        elif addressprompt_three == 4:
            # 6
            self.btn_prompt.clicked.connect(self.onTeoria4)
        elif addressprompt_three == 5:
            # 8
            self.btn_prompt.clicked.connect(self.onTeoria6)
        elif addressprompt_three == 6:
            # 9
            self.btn_prompt.clicked.connect(self.onTeoria7)
        elif addressprompt_three == 7:
            # 15
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_three == 8:
            # 17
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_three == 9:
            # 18
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_three == 10:
            # 19
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_three == 11:
            # 22
            self.btn_prompt.clicked.connect(self.onTeoria9)
        elif addressprompt_three == 12:
            # 23
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_three == 13:
            # 25
            self.btn_prompt.clicked.connect(self.onTeoria10)
        elif addressprompt_three == 14:
            # 26
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_three == 15:
            # 27
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_three == 16:
            # 28
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_three == 17:
            # 29
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_three == 18:
            # 30
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_three == 19:
            # 31
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_three == 20:
            # 33
            self.btn_prompt.clicked.connect(self.onTeoria11)
        elif addressprompt_three == 21:
            # 35
            self.btn_prompt.clicked.connect(self.onTeoria12)
        elif addressprompt_three == 22:
            # 37
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_three == 23:
            # 38
            self.btn_prompt.clicked.connect(self.onTeoria13)
        elif addressprompt_three == 24:
            # 60
            self.btn_prompt.clicked.connect(self.onTeoria18)
        elif addressprompt_three == 25:
            # 62
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_three == 26:
            # 65
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_three == 27:
            # 68
            self.btn_prompt.clicked.connect(self.onTeoria20)
        elif addressprompt_three == 28:
            # 69
            self.btn_prompt.clicked.connect(self.onTeoria21)
        elif addressprompt_three == 29:
            # 76
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_three == 30:
            # 77
            self.btn_prompt.clicked.connect(self.onTeoria23)
        elif addressprompt_three == 31:
            # 79
            self.btn_prompt.clicked.connect(self.onTeoria24)
        elif addressprompt_three == 32:
            # 80
            self.btn_prompt.clicked.connect(self.onTeoria25)
        elif addressprompt_three == 33:
            # 81
            self.btn_prompt.clicked.connect(self.onTeoria25)
        elif addressprompt_three == 34:
            # 83
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 35:
            # 84
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 36:
            # 85
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 37:
            # 86
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 38:
            # 87
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 39:
            # 88
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 40:
            # 89
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 41:
            # 90
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 42:
            # 93
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 43:
            # 94
            self.btn_prompt.clicked.connect(self.onTeoria26)
        elif addressprompt_three == 44:
            # 95
            self.btn_prompt.clicked.connect(self.onTeoria27)
        elif addressprompt_three == 45:
            # 96
            self.btn_prompt.clicked.connect(self.onTeoria27)
        elif addressprompt_three == 46:
            # 98
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_three == 47:
            # 100
            self.btn_prompt.clicked.connect(self.onTeoria30)
        elif addressprompt_three == 48:
            # 101
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_three == 49:
            # 102
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_three == 50:
            # 103
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_three == 51:
            # 104
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_three == 52:
            # 106
            self.btn_prompt.clicked.connect(self.onTeoria31)
        elif addressprompt_three == 53:
            # 108
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_three == 54:
            # 109
            self.btn_prompt.clicked.connect(self.onTeoria32)
        elif addressprompt_three == 55:
            # 116
            self.btn_prompt.clicked.connect(self.onTeoria34)
        elif addressprompt_three == 56:
            # 118
            self.btn_prompt.clicked.connect(self.onTeoria35)
        elif addressprompt_three == 57:
            # 119
            self.btn_prompt.clicked.connect(self.onTeoria36)
        elif addressprompt_three == 58:
            # 123
            self.btn_prompt.clicked.connect(self.onTeoria37)
        elif addressprompt_three == 59:
            # 124
            self.btn_prompt.clicked.connect(self.onTeoria38)
        elif addressprompt_three == 60:
            # 129
            self.btn_prompt.clicked.connect(self.onTeoria39)
        addressprompt_three += 1

    def onTeoria1(self):
        self.teoria_vp1 = TeoriaOneIII()
        self.teoria_vp1.show()

    def onTeoria2(self):
        self.teoria_vp2 = TeoriaTwoIII()
        self.teoria_vp2.show()

    def onTeoria3(self):
        self.teoria_vp3 = TeoriaThreeIII()
        self.teoria_vp3.show()

    def onTeoria4(self):
        self.teoria_vp4 = TeoriaFourIII()
        self.teoria_vp4.show()

    def onTeoria5(self):
        self.teoria_vp5 = TeoriaFiveIII()
        self.teoria_vp5.show()

    def onTeoria6(self):
        self.teoria_vp6 = TeoriaSixIII()
        self.teoria_vp6.show()

    def onTeoria7(self):
        self.teoria_vp7 = TeoriaSevenIII()
        self.teoria_vp7.show()

    def onTeoria8(self):
        self.teoria_vp8 = TeoriaEightIII()
        self.teoria_vp8.show()

    def onTeoria9(self):
        self.teoria_vp9 = TeoriaNineIII()
        self.teoria_vp9.show()

    def onTeoria10(self):
        self.teoria_vp10 = TeoriaTenIII()
        self.teoria_vp10.show()

    def onTeoria11(self):
        self.teoria_vp11 = TeoriaElevenIII()
        self.teoria_vp11.show()

    def onTeoria12(self):
        self.teoria_vp12 = TeoriaTwelveIII()
        self.teoria_vp12.show()

    def onTeoria13(self):
        self.teoria_vp13 = TeoriaThirteenIII()
        self.teoria_vp13.show()

    def onTeoria14(self):
        self.teoria_vp14 = TeoriaFourteenIII()
        self.teoria_vp14.show()

    def onTeoria15(self):
        self.teoria_vp15 = TeoriaFifteenIII()
        self.teoria_vp15.show()

    def onTeoria16(self):
        self.teoria_vp16 = TeoriaSixteenIII()
        self.teoria_vp16.show()

    def onTeoria17(self):
        self.teoria_vp17 = TeoriaSeventeenIII()
        self.teoria_vp17.show()

    def onTeoria18(self):
        self.teoria_vp18 = TeoriaEighteenIII()
        self.teoria_vp18.show()

    def onTeoria19(self):
        self.teoria_vp19 = TeoriaNineteenIII()
        self.teoria_vp19.show()

    def onTeoria20(self):
        self.teoria_vp20 = TeoriaTwentyIII()
        self.teoria_vp20.show()

    def onTeoria21(self):
        self.teoria_vp21 = TeoriaTwentyOneIII()
        self.teoria_vp21.show()

    def onTeoria22(self):
        self.teoria_vp22 = TeoriaTwentyTwoIII()
        self.teoria_vp22.show()

    def onTeoria23(self):
        self.teoria_vp23 = TeoriaTwentyThreeIII()
        self.teoria_vp23.show()

    def onTeoria24(self):
        self.teoria_vp24 = TeoriaTwentyFourIII()
        self.teoria_vp24.show()

    def onTeoria25(self):
        self.teoria_vp25 = TeoriaTwentyFiveIII()
        self.teoria_vp25.show()

    def onTeoria26(self):
        self.teoria_vp26 = TeoriaTwentySixIII()
        self.teoria_vp26.show()

    def onTeoria27(self):
        self.teoria_vp27 = TeoriaTwentySevenIII()
        self.teoria_vp27.show()

    def onTeoria28(self):
        self.teoria_vp28 = TeoriaTwentyEightIII()
        self.teoria_vp28.show()

    def onTeoria29(self):
        self.teoria_vp29 = TeoriaTwentyNineIII()
        self.teoria_vp29.show()

    def onTeoria30(self):
        self.teoria_vp30 = TeoriaThirtyIII()
        self.teoria_vp30.show()

    def onTeoria31(self):
        self.teoria_vp31 = TeoriaThirtyOneIII()
        self.teoria_vp31.show()

    def onTeoria32(self):
        self.teoria_vp32 = TeoriaThirtyTwoIII()
        self.teoria_vp32.show()

    def onTeoria33(self):
        self.teoria_vp33 = TeoriaThirtyThreeIII()
        self.teoria_vp33.show()

    def onTeoria34(self):
        self.teoria_vp34 = TeoriaThirtyFourIII()
        self.teoria_vp34.show()

    def onTeoria35(self):
        self.teoria_vp35 = TeoriaThirtyFiveIII()
        self.teoria_vp35.show()

    def onTeoria36(self):
        self.teoria_vp36 = TeoriaThirtySixIII()
        self.teoria_vp36.show()

    def onTeoria37(self):
        self.teoria_vp37 = TeoriaThirtySevenIII()
        self.teoria_vp37.show()

    def onTeoria38(self):
        self.teoria_vp38 = TeoriaThirtyEightIII()
        self.teoria_vp38.show()

    def onTeoria39(self):
        self.teoria_vp39 = TeoriaThirtyNineIII()
        self.teoria_vp39.show()

    #очистить выбор checkbox
    def clear(self):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)

    #подсчет правильных ответов
    def check_answer(self):
        if self.checkBox_1.text() in correct_answer and self.checkBox_2.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_1.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_1.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_2.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_2.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_3.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() == True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_1.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_2.text() in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_3.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()
        elif self.checkBox_4.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_1.text() not in correct_answer:
            if self.checkBox_4.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_1.isChecked() != True:
                self.right()
                self.clear()
                self.quantity_question()
            else:
                self.wrong()
                self.clear()

    #вывод экрана при нажатии ДАЛЕЕ
    def quantity_question(self):
        if numberprompt_three < len(questionsIII):
            self.choice_question_answers()
        elif numberprompt_three == len(questionsIII):
            self.resultatWindowIII()

    #экран 'Результат'
    def resultatWindowIII(self):
        self.RWindow = ResultatPromptIII()
        self.RWindow.show()
        self.close()
    #диалоговое окно ВЕРНО
    def right(self):
        self.onRight = Right()
        self.onRight.show()
    # диалоговое окно НЕВЕРНО
    def wrong(self):
        self.onWrong = Wrong()
        self.onWrong.show()

#окно 'Результат' режима 'Обучение и контроль' категории III
class ResultatPromptIII(QtWidgets.QMainWindow,Ui_ResultatPromWindow):
    def __init__(self):
        super(ResultatPromptIII, self).__init__()
        self.setupUi(self)

        self.btn_glavnaya.clicked.connect(self.returnGlavnayaIII)
        self.btn_again.clicked.connect(self.onAgainPrompt)

    def onAgainPrompt(self):
        self.on_again =TestPrompt_0III()
        self.on_again.show()
        self.close()

    def returnGlavnayaIII(self):
        self.return_glavnayaIII = Glavnaya_III()
        self.return_glavnayaIII.show()
        self.close()

#экран 'начать контрольный тест'категории III
class Test_0III(QtWidgets.QMainWindow,Ui_Test0Window):
    def __init__(self):
        super(Test_0III, self).__init__()
        self.setupUi(self)

        self.btn_begin_test.clicked.connect(self.begin_test)
        self.btn_glavnaya_test.clicked.connect(self.returnGlavnayaIII)

    def begin_test(self):
        global number_three
        number_three = 0
        global result_three
        result_three = 0
        self.test_3 = TestIII()
        self.test_3.show()
        self.close()

# переход к экрану 'главная III'
    def returnGlavnayaIII(self):
        self.GIII = Glavnaya_III()
        self.GIII.show()
        self.close()

#экран вопросы 'контрольный тест' категории III
class TestIII(QtWidgets.QMainWindow,Ui_TestWindow):
    def __init__(self):
        super(TestIII, self).__init__()
        self.setupUi(self)
        self.choice_question_answers()

        self.btn_dalee_test.clicked.connect(self.check_answer)
        self.btn_glavnaya_test.clicked.connect(self.returnGlavnaya)

    def returnGlavnaya(self):
        self.return_glavnaya = Glavnaya_III()
        self.return_glavnaya.show()
        self.close()

    def clear(self):
        self.checkBox_1.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.checkBox_4.setChecked(False)

    def choice_question_answers(self):
        question = random.choice(questionsIII)
        answers = question_answer[question]
        answer = random.sample(answers, len(answers))
        self.textQuestion.setText(question)
        self.checkBox_1.setText(answer[0]+';')
        self.checkBox_2.setText(answer[1]+';')
        self.checkBox_3.setText(answer[2]+';')
        self.checkBox_4.setText(answer[3]+'.')
        global number_three
        number_three = number_three+1
        self.label.setText(f'Вопрос № {number_three}')

    def check_answer(self):
        global result_three
        if self.checkBox_1.text() in correct_answer and self.checkBox_2.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() == True:
                result_three +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True:
                result_three +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_2.isChecked() == True:
                result_three +=0.5
            else:
                result_three +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() == True:
                result_three +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_3.isChecked() != True:
                result_three +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() == True:
                result_three +=0.5
            else:
                result_three +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_three +=1
            elif self.checkBox_1.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_three +=0.5
            elif self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_three +=0.5
            else:
                result_three +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_3.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() == True:
                result_three +=1
            elif self.checkBox_2.isChecked() == True and self.checkBox_3.isChecked() != True:
                result_three +=0.5
            elif self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() == True:
                result_three +=0.5
            else:
                result_three +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_three +=1
            elif self.checkBox_2.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_three +=0.5
            elif self.checkBox_2.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_three +=0.5
            else:
                result_three +=0
        elif self.checkBox_3.text() in correct_answer and self.checkBox_4.text() in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() == True:
                result_three +=1
            elif self.checkBox_3.isChecked() == True and self.checkBox_4.isChecked() != True:
                result_three +=0.5
            elif self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() == True:
                result_three +=0.5
            else:
                result_three +=0
        elif self.checkBox_1.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_1.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_three +=1
            else:
                result_three +=0
        elif self.checkBox_2.text() in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_2.isChecked() == True and self.checkBox_1.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_three +=1
            else:
                result_three +=0
        elif self.checkBox_3.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_1.text() not in correct_answer and self.checkBox_4.text() not in correct_answer:
            if self.checkBox_3.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_1.isChecked() != True and self.checkBox_4.isChecked() != True:
                result_three +=1
            else:
                result_three +=0
        elif self.checkBox_4.text() in correct_answer and self.checkBox_2.text() not in correct_answer and self.checkBox_3.text() not in correct_answer and self.checkBox_1.text() not in correct_answer:
            if self.checkBox_4.isChecked() == True and self.checkBox_2.isChecked() != True and self.checkBox_3.isChecked() != True and self.checkBox_1.isChecked() != True:
               result_three +=1
            else:
                result_three +=0
        self.clear()
        self.quantity_question()

    def quantity_question(self):
        if number_three < 20:
            self.choice_question_answers()
        elif number_three == 20:
            self.resultatWindowIII()

    def resultatWindowIII(self):
        self.RWindow = ResultatIII()
        self.RWindow.show()
        self.close()

#экран 'результат контрольного теста' категория III
class ResultatIII(QtWidgets.QMainWindow,Ui_ResultatWindow):
    def __init__(self):
        super(ResultatIII, self).__init__()
        self.setupUi(self)
        self.result.setText(str(result_three) + ' из 20.0')


        self.btn_glavnaya.clicked.connect(self.returnGlavnayaIII)
        self.btn_again.clicked.connect(self.onAgain)

    def onAgain(self):
        self.on_again = Test_0III()
        self.on_again.show()
        self.close()

    def returnGlavnayaIII(self):
        self.return_glavnayaIII = Glavnaya_III()
        self.return_glavnayaIII.show()
        self.close()

#список вопросов категории I
class QuestionsI(QtWidgets.QMainWindow,Ui_QuestionsIWindow):
    def __init__(self):
        super(QuestionsI, self).__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.question1)
        self.btn_2.clicked.connect(self.question2)
        self.btn_3.clicked.connect(self.question3)
        self.btn_4.clicked.connect(self.question4)
        self.btn_5.clicked.connect(self.question5)
        self.btn_6.clicked.connect(self.question6)
        self.btn_7.clicked.connect(self.question7)
        self.btn_8.clicked.connect(self.question8)
        self.btn_9.clicked.connect(self.question9)
        self.btn_10.clicked.connect(self.question10)
        self.btn_11.clicked.connect(self.question11)
        self.btn_12.clicked.connect(self.question12)
        self.btn_13.clicked.connect(self.question13)
        self.btn_14.clicked.connect(self.question14)
        self.btn_15.clicked.connect(self.question15)
        self.btn_16.clicked.connect(self.question16)
        self.btn_17.clicked.connect(self.question17)
        self.btn_18.clicked.connect(self.question18)
        self.btn_19.clicked.connect(self.question19)
        self.btn_20.clicked.connect(self.question20)
        self.btn_21.clicked.connect(self.question21)
        self.btn_22.clicked.connect(self.question22)
        self.btn_23.clicked.connect(self.question23)
        self.btn_24.clicked.connect(self.question24)
        self.btn_25.clicked.connect(self.question25)
        self.btn_26.clicked.connect(self.question26)
        self.btn_27.clicked.connect(self.question27)
        self.btn_28.clicked.connect(self.question28)
        self.btn_29.clicked.connect(self.question29)
        self.btn_30.clicked.connect(self.question30)
        self.btn_31.clicked.connect(self.question31)
        self.btn_32.clicked.connect(self.question32)
        self.btn_33.clicked.connect(self.question33)
        self.btn_34.clicked.connect(self.question34)
        self.btn_35.clicked.connect(self.question35)
        self.btn_36.clicked.connect(self.question36)
        self.btn_37.clicked.connect(self.question37)
        self.btn_38.clicked.connect(self.question38)
        self.btn_39.clicked.connect(self.question39)
        self.btn_40.clicked.connect(self.question40)
        self.btn_41.clicked.connect(self.question41)
        self.btn_42.clicked.connect(self.question42)
        self.btn_43.clicked.connect(self.question43)
        self.btn_44.clicked.connect(self.question44)
        self.btn_45.clicked.connect(self.question45)
        self.btn_46.clicked.connect(self.question46)
        self.btn_47.clicked.connect(self.question47)
        self.btn_48.clicked.connect(self.question48)
        self.btn_49.clicked.connect(self.question49)
        self.btn_50.clicked.connect(self.question50)
        self.btn_51.clicked.connect(self.question51)
        self.btn_52.clicked.connect(self.question52)
        self.btn_53.clicked.connect(self.question53)
        self.btn_54.clicked.connect(self.question54)
        self.btn_55.clicked.connect(self.question55)
        self.btn_56.clicked.connect(self.question56)
        self.btn_57.clicked.connect(self.question57)
        self.btn_58.clicked.connect(self.question58)
        self.btn_59.clicked.connect(self.question59)
        self.btn_60.clicked.connect(self.question60)
        self.btn_62.clicked.connect(self.question62)
        self.btn_63.clicked.connect(self.question63)
        self.btn_64.clicked.connect(self.question64)
        self.btn_65.clicked.connect(self.question65)
        self.btn_66.clicked.connect(self.question66)
        self.btn_67.clicked.connect(self.question67)
        self.btn_68.clicked.connect(self.question68)
        self.btn_69.clicked.connect(self.question69)
        self.btn_70.clicked.connect(self.question70)
        self.btn_71.clicked.connect(self.question71)
        self.btn_72.clicked.connect(self.question72)
        self.btn_73.clicked.connect(self.question73)
        self.btn_74.clicked.connect(self.question74)
        self.btn_75.clicked.connect(self.question75)
        self.btn_76.clicked.connect(self.question76)
        self.btn_77.clicked.connect(self.question77)
        self.btn_78.clicked.connect(self.question78)
        self.btn_79.clicked.connect(self.question79)
        self.btn_80.clicked.connect(self.question80)
        self.btn_81.clicked.connect(self.question81)
        self.btn_82.clicked.connect(self.question82)
        self.btn_83.clicked.connect(self.question83)
        self.btn_84.clicked.connect(self.question84)
        self.btn_85.clicked.connect(self.question85)
        self.btn_86.clicked.connect(self.question86)
        self.btn_87.clicked.connect(self.question87)
        self.btn_88.clicked.connect(self.question88)
        self.btn_89.clicked.connect(self.question89)
        self.btn_90.clicked.connect(self.question90)
        self.btn_91.clicked.connect(self.question91)
        self.btn_92.clicked.connect(self.question92)
        self.btn_93.clicked.connect(self.question93)
        self.btn_94.clicked.connect(self.question94)
        self.btn_95.clicked.connect(self.question95)
        self.btn_96.clicked.connect(self.question96)
        self.btn_97.clicked.connect(self.question97)
        self.btn_98.clicked.connect(self.question98)
        self.btn_99.clicked.connect(self.question99)
        self.btn_100.clicked.connect(self.question100)
        self.btn_101.clicked.connect(self.question101)
        self.btn_102.clicked.connect(self.question102)
        self.btn_103.clicked.connect(self.question103)
        self.btn_104.clicked.connect(self.question104)
        self.btn_105.clicked.connect(self.question105)
        self.btn_106.clicked.connect(self.question106)
        self.btn_107.clicked.connect(self.question107)
        self.btn_108.clicked.connect(self.question108)
        self.btn_109.clicked.connect(self.question109)
        self.btn_110.clicked.connect(self.question110)
        self.btn_111.clicked.connect(self.question111)
        self.btn_112.clicked.connect(self.question112)
        self.btn_113.clicked.connect(self.question113)
        self.btn_114.clicked.connect(self.question114)
        self.btn_115.clicked.connect(self.question115)
        self.btn_116.clicked.connect(self.question116)
        self.btn_117.clicked.connect(self.question117)
        self.btn_118.clicked.connect(self.question118)
        self.btn_119.clicked.connect(self.question119)
        self.btn_120.clicked.connect(self.question120)
        self.btn_121.clicked.connect(self.question121)
        self.btn_122.clicked.connect(self.question122)
        self.btn_123.clicked.connect(self.question123)
        self.btn_124.clicked.connect(self.question124)
        self.btn_125.clicked.connect(self.question125)
        self.btn_126.clicked.connect(self.question126)
        self.btn_127.clicked.connect(self.question127)
        self.btn_128.clicked.connect(self.question128)
        self.btn_129.clicked.connect(self.question129)

    def question1(self):
        global addressprompt_one
        addressprompt_one = 0
        global numberprompt_one
        numberprompt_one = 0
        self.question1 = TestPromptI()
        self.question1.show()

    def question2(self):
        global addressprompt_one
        addressprompt_one = 1
        global numberprompt_one
        numberprompt_one = 1
        self.question1 = TestPromptI()
        self.question1.show()

    def question3(self):
        global addressprompt_one
        addressprompt_one = 2
        global numberprompt_one
        numberprompt_one = 2
        self.question1 = TestPromptI()
        self.question1.show()

    def question4(self):
        global addressprompt_one
        addressprompt_one = 3
        global numberprompt_one
        numberprompt_one = 3
        self.question1 = TestPromptI()
        self.question1.show()

    def question5(self):
        global addressprompt_one
        addressprompt_one = 4
        global numberprompt_one
        numberprompt_one = 4
        self.question1 = TestPromptI()
        self.question1.show()

    def question6(self):
        global addressprompt_one
        addressprompt_one = 5
        global numberprompt_one
        numberprompt_one = 5
        self.question1 = TestPromptI()
        self.question1.show()

    def question7(self):
        global addressprompt_one
        addressprompt_one = 6
        global numberprompt_one
        numberprompt_one = 6
        self.question1 = TestPromptI()
        self.question1.show()

    def question8(self):
        global addressprompt_one
        addressprompt_one = 7
        global numberprompt_one
        numberprompt_one = 7
        self.question1 = TestPromptI()
        self.question1.show()

    def question9(self):
        global addressprompt_one
        addressprompt_one = 8
        global numberprompt_one
        numberprompt_one = 8
        self.question1 = TestPromptI()
        self.question1.show()

    def question10(self):
        global addressprompt_one
        addressprompt_one = 9
        global numberprompt_one
        numberprompt_one = 9
        self.question1 = TestPromptI()
        self.question1.show()

    def question11(self):
        global addressprompt_one
        addressprompt_one = 10
        global numberprompt_one
        numberprompt_one = 10
        self.question1 = TestPromptI()
        self.question1.show()

    def question12(self):
        global addressprompt_one
        addressprompt_one = 11
        global numberprompt_one
        numberprompt_one = 11
        self.question1 = TestPromptI()
        self.question1.show()

    def question13(self):
        global addressprompt_one
        addressprompt_one = 12
        global numberprompt_one
        numberprompt_one = 12
        self.question1 = TestPromptI()
        self.question1.show()

    def question14(self):
        global addressprompt_one
        addressprompt_one = 13
        global numberprompt_one
        numberprompt_one = 13
        self.question1 = TestPromptI()
        self.question1.show()

    def question15(self):
        global addressprompt_one
        addressprompt_one = 14
        global numberprompt_one
        numberprompt_one = 14
        self.question1 = TestPromptI()
        self.question1.show()

    def question16(self):
        global addressprompt_one
        addressprompt_one = 15
        global numberprompt_one
        numberprompt_one = 15
        self.question1 = TestPromptI()
        self.question1.show()

    def question17(self):
        global addressprompt_one
        addressprompt_one = 16
        global numberprompt_one
        numberprompt_one = 16
        self.question1 = TestPromptI()
        self.question1.show()

    def question18(self):
        global addressprompt_one
        addressprompt_one = 17
        global numberprompt_one
        numberprompt_one = 17
        self.question1 = TestPromptI()
        self.question1.show()

    def question19(self):
        global addressprompt_one
        addressprompt_one = 18
        global numberprompt_one
        numberprompt_one = 18
        self.question1 = TestPromptI()
        self.question1.show()

    def question20(self):
        global addressprompt_one
        addressprompt_one = 19
        global numberprompt_one
        numberprompt_one = 19
        self.question1 = TestPromptI()
        self.question1.show()

    def question21(self):
        global addressprompt_one
        addressprompt_one = 20
        global numberprompt_one
        numberprompt_one = 20
        self.question1 = TestPromptI()
        self.question1.show()

    def question22(self):
        global addressprompt_one
        addressprompt_one = 21
        global numberprompt_one
        numberprompt_one = 21
        self.question1 = TestPromptI()
        self.question1.show()

    def question23(self):
        global addressprompt_one
        addressprompt_one = 22
        global numberprompt_one
        numberprompt_one = 22
        self.question1 = TestPromptI()
        self.question1.show()

    def question24(self):
        global addressprompt_one
        addressprompt_one = 23
        global numberprompt_one
        numberprompt_one = 23
        self.question1 = TestPromptI()
        self.question1.show()

    def question25(self):
        global addressprompt_one
        addressprompt_one = 24
        global numberprompt_one
        numberprompt_one = 24
        self.question1 = TestPromptI()
        self.question1.show()

    def question26(self):
        global addressprompt_one
        addressprompt_one = 25
        global numberprompt_one
        numberprompt_one = 25
        self.question1 = TestPromptI()
        self.question1.show()

    def question27(self):
        global addressprompt_one
        addressprompt_one = 26
        global numberprompt_one
        numberprompt_one = 26
        self.question1 = TestPromptI()
        self.question1.show()

    def question28(self):
        global addressprompt_one
        addressprompt_one = 27
        global numberprompt_one
        numberprompt_one = 27
        self.question1 = TestPromptI()
        self.question1.show()

    def question29(self):
        global addressprompt_one
        addressprompt_one = 28
        global numberprompt_one
        numberprompt_one = 28
        self.question1 = TestPromptI()
        self.question1.show()

    def question30(self):
        global addressprompt_one
        addressprompt_one = 29
        global numberprompt_one
        numberprompt_one = 29
        self.question1 = TestPromptI()
        self.question1.show()

    def question31(self):
        global addressprompt_one
        addressprompt_one = 30
        global numberprompt_one
        numberprompt_one = 30
        self.question1 = TestPromptI()
        self.question1.show()

    def question32(self):
        global addressprompt_one
        addressprompt_one = 31
        global numberprompt_one
        numberprompt_one = 31
        self.question1 = TestPromptI()
        self.question1.show()

    def question33(self):
        global addressprompt_one
        addressprompt_one = 32
        global numberprompt_one
        numberprompt_one = 32
        self.question1 = TestPromptI()
        self.question1.show()

    def question34(self):
        global addressprompt_one
        addressprompt_one = 33
        global numberprompt_one
        numberprompt_one = 33
        self.question1 = TestPromptI()
        self.question1.show()

    def question35(self):
        global addressprompt_one
        addressprompt_one = 34
        global numberprompt_one
        numberprompt_one = 34
        self.question1 = TestPromptI()
        self.question1.show()

    def question36(self):
        global addressprompt_one
        addressprompt_one = 35
        global numberprompt_one
        numberprompt_one = 35
        self.question1 = TestPromptI()
        self.question1.show()

    def question37(self):
        global addressprompt_one
        addressprompt_one = 36
        global numberprompt_one
        numberprompt_one = 36
        self.question1 = TestPromptI()
        self.question1.show()

    def question38(self):
        global addressprompt_one
        addressprompt_one = 37
        global numberprompt_one
        numberprompt_one = 37
        self.question1 = TestPromptI()
        self.question1.show()

    def question39(self):
        global addressprompt_one
        addressprompt_one = 38
        global numberprompt_one
        numberprompt_one = 38
        self.question1 = TestPromptI()
        self.question1.show()

    def question40(self):
        global addressprompt_one
        addressprompt_one = 39
        global numberprompt_one
        numberprompt_one = 39
        self.question1 = TestPromptI()
        self.question1.show()

    def question41(self):
        global addressprompt_one
        addressprompt_one = 40
        global numberprompt_one
        numberprompt_one = 40
        self.question1 = TestPromptI()
        self.question1.show()

    def question42(self):
        global addressprompt_one
        addressprompt_one = 41
        global numberprompt_one
        numberprompt_one = 41
        self.question1 = TestPromptI()
        self.question1.show()

    def question43(self):
        global addressprompt_one
        addressprompt_one = 42
        global numberprompt_one
        numberprompt_one = 42
        self.question1 = TestPromptI()
        self.question1.show()

    def question44(self):
        global addressprompt_one
        addressprompt_one = 43
        global numberprompt_one
        numberprompt_one = 43
        self.question1 = TestPromptI()
        self.question1.show()

    def question45(self):
        global addressprompt_one
        addressprompt_one = 44
        global numberprompt_one
        numberprompt_one = 44
        self.question1 = TestPromptI()
        self.question1.show()

    def question46(self):
        global addressprompt_one
        addressprompt_one = 45
        global numberprompt_one
        numberprompt_one = 45
        self.question1 = TestPromptI()
        self.question1.show()

    def question47(self):
        global addressprompt_one
        addressprompt_one = 46
        global numberprompt_one
        numberprompt_one = 46
        self.question1 = TestPromptI()
        self.question1.show()

    def question48(self):
        global addressprompt_one
        addressprompt_one = 47
        global numberprompt_one
        numberprompt_one = 47
        self.question1 = TestPromptI()
        self.question1.show()

    def question49(self):
        global addressprompt_one
        addressprompt_one = 48
        global numberprompt_one
        numberprompt_one = 48
        self.question1 = TestPromptI()
        self.question1.show()

    def question50(self):
        global addressprompt_one
        addressprompt_one = 49
        global numberprompt_one
        numberprompt_one = 49
        self.question1 = TestPromptI()
        self.question1.show()

    def question51(self):
        global addressprompt_one
        addressprompt_one = 50
        global numberprompt_one
        numberprompt_one = 50
        self.question1 = TestPromptI()
        self.question1.show()

    def question52(self):
        global addressprompt_one
        addressprompt_one = 51
        global numberprompt_one
        numberprompt_one = 51
        self.question1 = TestPromptI()
        self.question1.show()

    def question53(self):
        global addressprompt_one
        addressprompt_one = 52
        global numberprompt_one
        numberprompt_one = 52
        self.question1 = TestPromptI()
        self.question1.show()

    def question54(self):
        global addressprompt_one
        addressprompt_one = 53
        global numberprompt_one
        numberprompt_one = 53
        self.question1 = TestPromptI()
        self.question1.show()

    def question55(self):
        global addressprompt_one
        addressprompt_one = 54
        global numberprompt_one
        numberprompt_one = 54
        self.question1 = TestPromptI()
        self.question1.show()

    def question56(self):
        global addressprompt_one
        addressprompt_one = 55
        global numberprompt_one
        numberprompt_one = 55
        self.question1 = TestPromptI()
        self.question1.show()

    def question57(self):
        global addressprompt_one
        addressprompt_one = 56
        global numberprompt_one
        numberprompt_one = 56
        self.question1 = TestPromptI()
        self.question1.show()

    def question58(self):
        global addressprompt_one
        addressprompt_one = 57
        global numberprompt_one
        numberprompt_one = 57
        self.question1 = TestPromptI()
        self.question1.show()

    def question59(self):
        global addressprompt_one
        addressprompt_one = 58
        global numberprompt_one
        numberprompt_one = 58
        self.question1 = TestPromptI()
        self.question1.show()

    def question60(self):
        global addressprompt_one
        addressprompt_one = 59
        global numberprompt_one
        numberprompt_one = 59
        self.question1 = TestPromptI()
        self.question1.show()

    def question61(self):
        global addressprompt_one
        addressprompt_one = 60
        global numberprompt_one
        numberprompt_one = 60
        self.question1 = TestPromptI()
        self.question1.show()

    def question62(self):
        global addressprompt_one
        addressprompt_one = 61
        global numberprompt_one
        numberprompt_one = 61
        self.question1 = TestPromptI()
        self.question1.show()

    def question63(self):
        global addressprompt_one
        addressprompt_one = 62
        global numberprompt_one
        numberprompt_one = 62
        self.question1 = TestPromptI()
        self.question1.show()

    def question64(self):
        global addressprompt_one
        addressprompt_one = 63
        global numberprompt_one
        numberprompt_one = 63
        self.question1 = TestPromptI()
        self.question1.show()

    def question65(self):
        global addressprompt_one
        addressprompt_one = 64
        global numberprompt_one
        numberprompt_one = 64
        self.question1 = TestPromptI()
        self.question1.show()

    def question66(self):
        global addressprompt_one
        addressprompt_one = 65
        global numberprompt_one
        numberprompt_one = 65
        self.question1 = TestPromptI()
        self.question1.show()

    def question67(self):
        global addressprompt_one
        addressprompt_one = 66
        global numberprompt_one
        numberprompt_one = 66
        self.question1 = TestPromptI()
        self.question1.show()

    def question68(self):
        global addressprompt_one
        addressprompt_one = 67
        global numberprompt_one
        numberprompt_one = 67
        self.question1 = TestPromptI()
        self.question1.show()

    def question69(self):
        global addressprompt_one
        addressprompt_one = 68
        global numberprompt_one
        numberprompt_one = 68
        self.question1 = TestPromptI()
        self.question1.show()

    def question70(self):
        global addressprompt_one
        addressprompt_one = 69
        global numberprompt_one
        numberprompt_one = 69
        self.question1 = TestPromptI()
        self.question1.show()

    def question71(self):
        global addressprompt_one
        addressprompt_one = 70
        global numberprompt_one
        numberprompt_one = 70
        self.question1 = TestPromptI()
        self.question1.show()

    def question72(self):
        global addressprompt_one
        addressprompt_one = 71
        global numberprompt_one
        numberprompt_one = 71
        self.question1 = TestPromptI()
        self.question1.show()

    def question73(self):
        global addressprompt_one
        addressprompt_one = 72
        global numberprompt_one
        numberprompt_one = 72
        self.question1 = TestPromptI()
        self.question1.show()

    def question74(self):
        global addressprompt_one
        addressprompt_one = 73
        global numberprompt_one
        numberprompt_one = 73
        self.question1 = TestPromptI()
        self.question1.show()

    def question75(self):
        global addressprompt_one
        addressprompt_one = 74
        global numberprompt_one
        numberprompt_one = 74
        self.question1 = TestPromptI()
        self.question1.show()

    def question76(self):
        global addressprompt_one
        addressprompt_one = 75
        global numberprompt_one
        numberprompt_one = 75
        self.question1 = TestPromptI()
        self.question1.show()

    def question77(self):
        global addressprompt_one
        addressprompt_one = 76
        global numberprompt_one
        numberprompt_one = 76
        self.question1 = TestPromptI()
        self.question1.show()

    def question78(self):
        global addressprompt_one
        addressprompt_one = 77
        global numberprompt_one
        numberprompt_one = 77
        self.question1 = TestPromptI()
        self.question1.show()

    def question79(self):
        global addressprompt_one
        addressprompt_one = 78
        global numberprompt_one
        numberprompt_one = 78
        self.question1 = TestPromptI()
        self.question1.show()

    def question80(self):
        global addressprompt_one
        addressprompt_one = 79
        global numberprompt_one
        numberprompt_one = 79
        self.question1 = TestPromptI()
        self.question1.show()

    def question81(self):
        global addressprompt_one
        addressprompt_one = 80
        global numberprompt_one
        numberprompt_one = 80
        self.question1 = TestPromptI()
        self.question1.show()

    def question82(self):
        global addressprompt_one
        addressprompt_one = 81
        global numberprompt_one
        numberprompt_one = 81
        self.question1 = TestPromptI()
        self.question1.show()

    def question83(self):
        global addressprompt_one
        addressprompt_one = 82
        global numberprompt_one
        numberprompt_one = 82
        self.question1 = TestPromptI()
        self.question1.show()

    def question84(self):
        global addressprompt_one
        addressprompt_one = 83
        global numberprompt_one
        numberprompt_one = 83
        self.question1 = TestPromptI()
        self.question1.show()

    def question85(self):
        global addressprompt_one
        addressprompt_one = 84
        global numberprompt_one
        numberprompt_one = 84
        self.question1 = TestPromptI()
        self.question1.show()

    def question86(self):
        global addressprompt_one
        addressprompt_one = 85
        global numberprompt_one
        numberprompt_one = 85
        self.question1 = TestPromptI()
        self.question1.show()

    def question87(self):
        global addressprompt_one
        addressprompt_one = 86
        global numberprompt_one
        numberprompt_one = 86
        self.question1 = TestPromptI()
        self.question1.show()

    def question88(self):
        global addressprompt_one
        addressprompt_one = 87
        global numberprompt_one
        numberprompt_one = 87
        self.question1 = TestPromptI()
        self.question1.show()

    def question89(self):
        global addressprompt_one
        addressprompt_one = 88
        global numberprompt_one
        numberprompt_one = 88
        self.question1 = TestPromptI()
        self.question1.show()

    def question90(self):
        global addressprompt_one
        addressprompt_one = 89
        global numberprompt_one
        numberprompt_one = 89
        self.question1 = TestPromptI()
        self.question1.show()

    def question91(self):
        global addressprompt_one
        addressprompt_one = 90
        global numberprompt_one
        numberprompt_one = 90
        self.question1 = TestPromptI()
        self.question1.show()

    def question92(self):
        global addressprompt_one
        addressprompt_one = 91
        global numberprompt_one
        numberprompt_one = 91
        self.question1 = TestPromptI()
        self.question1.show()

    def question93(self):
        global addressprompt_one
        addressprompt_one = 92
        global numberprompt_one
        numberprompt_one = 92
        self.question1 = TestPromptI()
        self.question1.show()

    def question94(self):
        global addressprompt_one
        addressprompt_one = 93
        global numberprompt_one
        numberprompt_one = 93
        self.question1 = TestPromptI()
        self.question1.show()

    def question95(self):
        global addressprompt_one
        addressprompt_one = 94
        global numberprompt_one
        numberprompt_one = 94
        self.question1 = TestPromptI()
        self.question1.show()

    def question96(self):
        global addressprompt_one
        addressprompt_one = 95
        global numberprompt_one
        numberprompt_one = 95
        self.question1 = TestPromptI()
        self.question1.show()

    def question97(self):
        global addressprompt_one
        addressprompt_one = 96
        global numberprompt_one
        numberprompt_one = 96
        self.question1 = TestPromptI()
        self.question1.show()

    def question98(self):
        global addressprompt_one
        addressprompt_one = 97
        global numberprompt_one
        numberprompt_one = 97
        self.question1 = TestPromptI()
        self.question1.show()

    def question99(self):
        global addressprompt_one
        addressprompt_one = 98
        global numberprompt_one
        numberprompt_one = 98
        self.question1 = TestPromptI()
        self.question1.show()

    def question100(self):
        global addressprompt_one
        addressprompt_one = 99
        global numberprompt_one
        numberprompt_one = 99
        self.question1 = TestPromptI()
        self.question1.show()

    def question101(self):
        global addressprompt_one
        addressprompt_one = 100
        global numberprompt_one
        numberprompt_one = 100
        self.question1 = TestPromptI()
        self.question1.show()

    def question102(self):
        global addressprompt_one
        addressprompt_one = 101
        global numberprompt_one
        numberprompt_one = 101
        self.question1 = TestPromptI()
        self.question1.show()

    def question103(self):
        global addressprompt_one
        addressprompt_one = 102
        global numberprompt_one
        numberprompt_one = 102
        self.question1 = TestPromptI()
        self.question1.show()

    def question104(self):
        global addressprompt_one
        addressprompt_one = 103
        global numberprompt_one
        numberprompt_one = 103
        self.question1 = TestPromptI()
        self.question1.show()

    def question105(self):
        global addressprompt_one
        addressprompt_one = 104
        global numberprompt_one
        numberprompt_one = 104
        self.question1 = TestPromptI()
        self.question1.show()

    def question106(self):
        global addressprompt_one
        addressprompt_one = 105
        global numberprompt_one
        numberprompt_one = 105
        self.question1 = TestPromptI()
        self.question1.show()

    def question107(self):
        global addressprompt_one
        addressprompt_one = 106
        global numberprompt_one
        numberprompt_one = 106
        self.question1 = TestPromptI()
        self.question1.show()

    def question108(self):
        global addressprompt_one
        addressprompt_one = 107
        global numberprompt_one
        numberprompt_one = 107
        self.question1 = TestPromptI()
        self.question1.show()

    def question109(self):
        global addressprompt_one
        addressprompt_one = 108
        global numberprompt_one
        numberprompt_one = 108
        self.question1 = TestPromptI()
        self.question1.show()

    def question110(self):
        global addressprompt_one
        addressprompt_one = 109
        global numberprompt_one
        numberprompt_one = 109
        self.question1 = TestPromptI()
        self.question1.show()

    def question111(self):
        global addressprompt_one
        addressprompt_one = 110
        global numberprompt_one
        numberprompt_one = 110
        self.question1 = TestPromptI()
        self.question1.show()

    def question112(self):
        global addressprompt_one
        addressprompt_one = 111
        global numberprompt_one
        numberprompt_one = 111
        self.question1 = TestPromptI()
        self.question1.show()

    def question113(self):
        global addressprompt_one
        addressprompt_one = 112
        global numberprompt_one
        numberprompt_one = 112
        self.question1 = TestPromptI()
        self.question1.show()

    def question114(self):
        global addressprompt_one
        addressprompt_one = 113
        global numberprompt_one
        numberprompt_one = 113
        self.question1 = TestPromptI()
        self.question1.show()

    def question115(self):
        global addressprompt_one
        addressprompt_one = 114
        global numberprompt_one
        numberprompt_one = 114
        self.question1 = TestPromptI()
        self.question1.show()

    def question116(self):
        global addressprompt_one
        addressprompt_one = 115
        global numberprompt_one
        numberprompt_one = 115
        self.question1 = TestPromptI()
        self.question1.show()

    def question117(self):
        global addressprompt_one
        addressprompt_one = 116
        global numberprompt_one
        numberprompt_one = 116
        self.question1 = TestPromptI()
        self.question1.show()

    def question118(self):
        global addressprompt_one
        addressprompt_one = 117
        global numberprompt_one
        numberprompt_one = 117
        self.question1 = TestPromptI()
        self.question1.show()

    def question119(self):
        global addressprompt_one
        addressprompt_one = 118
        global numberprompt_one
        numberprompt_one = 118
        self.question1 = TestPromptI()
        self.question1.show()

    def question120(self):
        global addressprompt_one
        addressprompt_one = 119
        global numberprompt_one
        numberprompt_one = 119
        self.question1 = TestPromptI()
        self.question1.show()

    def question121(self):
        global addressprompt_one
        addressprompt_one = 120
        global numberprompt_one
        numberprompt_one = 120
        self.question1 = TestPromptI()
        self.question1.show()

    def question122(self):
        global addressprompt_one
        addressprompt_one = 121
        global numberprompt_one
        numberprompt_one = 121
        self.question1 = TestPromptI()
        self.question1.show()

    def question123(self):
        global addressprompt_one
        addressprompt_one = 122
        global numberprompt_one
        numberprompt_one = 122
        self.question1 = TestPromptI()
        self.question1.show()

    def question124(self):
        global addressprompt_one
        addressprompt_one = 123
        global numberprompt_one
        numberprompt_one = 123
        self.question1 = TestPromptI()
        self.question1.show()

    def question125(self):
        global addressprompt_one
        addressprompt_one = 124
        global numberprompt_one
        numberprompt_one = 124
        self.question1 = TestPromptI()
        self.question1.show()

    def question126(self):
        global addressprompt_one
        addressprompt_one = 125
        global numberprompt_one
        numberprompt_one = 125
        self.question1 = TestPromptI()
        self.question1.show()

    def question127(self):
        global addressprompt_one
        addressprompt_one = 126
        global numberprompt_one
        numberprompt_one = 126
        self.question1 = TestPromptI()
        self.question1.show()

    def question128(self):
        global addressprompt_one
        addressprompt_one = 127
        global numberprompt_one
        numberprompt_one = 127
        self.question1 = TestPromptI()
        self.question1.show()

    def question129(self):
        global addressprompt_one
        addressprompt_one = 128
        global numberprompt_one
        numberprompt_one = 128
        self.question1 = TestPromptI()
        self.question1.show()

#список вопросов категории II
class QuestionsII(QtWidgets.QMainWindow,Ui_QuestionsIIWindow):
    def __init__(self):
        super(QuestionsII, self).__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.question1)
        self.btn_2.clicked.connect(self.question2)
        self.btn_3.clicked.connect(self.question3)
        self.btn_4.clicked.connect(self.question4)
        self.btn_5.clicked.connect(self.question5)
        self.btn_6.clicked.connect(self.question6)
        self.btn_7.clicked.connect(self.question7)
        self.btn_8.clicked.connect(self.question8)
        self.btn_9.clicked.connect(self.question9)
        self.btn_10.clicked.connect(self.question10)
        self.btn_11.clicked.connect(self.question11)
        self.btn_12.clicked.connect(self.question12)
        self.btn_13.clicked.connect(self.question13)
        self.btn_14.clicked.connect(self.question14)
        self.btn_15.clicked.connect(self.question15)
        self.btn_16.clicked.connect(self.question16)
        self.btn_17.clicked.connect(self.question17)
        self.btn_18.clicked.connect(self.question18)
        self.btn_19.clicked.connect(self.question19)
        self.btn_20.clicked.connect(self.question20)
        self.btn_21.clicked.connect(self.question21)
        self.btn_22.clicked.connect(self.question22)
        self.btn_23.clicked.connect(self.question23)
        self.btn_24.clicked.connect(self.question24)
        self.btn_25.clicked.connect(self.question25)
        self.btn_26.clicked.connect(self.question26)
        self.btn_27.clicked.connect(self.question27)
        self.btn_28.clicked.connect(self.question28)
        self.btn_29.clicked.connect(self.question29)
        self.btn_30.clicked.connect(self.question30)
        self.btn_31.clicked.connect(self.question31)
        self.btn_32.clicked.connect(self.question32)
        self.btn_33.clicked.connect(self.question33)
        self.btn_34.clicked.connect(self.question34)
        self.btn_35.clicked.connect(self.question35)
        self.btn_36.clicked.connect(self.question36)
        self.btn_37.clicked.connect(self.question37)
        self.btn_38.clicked.connect(self.question38)
        self.btn_39.clicked.connect(self.question39)
        self.btn_40.clicked.connect(self.question40)
        self.btn_41.clicked.connect(self.question41)
        self.btn_42.clicked.connect(self.question42)
        self.btn_43.clicked.connect(self.question43)
        self.btn_44.clicked.connect(self.question44)
        self.btn_45.clicked.connect(self.question45)
        self.btn_46.clicked.connect(self.question46)
        self.btn_47.clicked.connect(self.question47)
        self.btn_48.clicked.connect(self.question48)
        self.btn_49.clicked.connect(self.question49)
        self.btn_50.clicked.connect(self.question50)
        self.btn_51.clicked.connect(self.question51)
        self.btn_52.clicked.connect(self.question52)
        self.btn_53.clicked.connect(self.question53)
        self.btn_54.clicked.connect(self.question54)
        self.btn_55.clicked.connect(self.question55)
        self.btn_56.clicked.connect(self.question56)
        self.btn_57.clicked.connect(self.question57)
        self.btn_58.clicked.connect(self.question58)
        self.btn_59.clicked.connect(self.question59)
        self.btn_60.clicked.connect(self.question60)
        self.btn_61.clicked.connect(self.question61)
        self.btn_62.clicked.connect(self.question62)
        self.btn_63.clicked.connect(self.question63)
        self.btn_64.clicked.connect(self.question64)
        self.btn_65.clicked.connect(self.question65)
        self.btn_66.clicked.connect(self.question66)
        self.btn_67.clicked.connect(self.question67)
        self.btn_68.clicked.connect(self.question68)
        self.btn_69.clicked.connect(self.question69)
        self.btn_70.clicked.connect(self.question70)
        self.btn_71.clicked.connect(self.question71)
        self.btn_72.clicked.connect(self.question72)
        self.btn_73.clicked.connect(self.question73)
        self.btn_74.clicked.connect(self.question74)
        self.btn_75.clicked.connect(self.question75)
        self.btn_76.clicked.connect(self.question76)
        self.btn_77.clicked.connect(self.question77)
        self.btn_78.clicked.connect(self.question78)
        self.btn_79.clicked.connect(self.question79)
        self.btn_80.clicked.connect(self.question80)
        self.btn_81.clicked.connect(self.question81)
        self.btn_82.clicked.connect(self.question82)
        self.btn_83.clicked.connect(self.question83)
        self.btn_84.clicked.connect(self.question84)
        self.btn_85.clicked.connect(self.question85)
        self.btn_86.clicked.connect(self.question86)
        self.btn_87.clicked.connect(self.question87)
        self.btn_88.clicked.connect(self.question88)
        self.btn_89.clicked.connect(self.question89)
        self.btn_90.clicked.connect(self.question90)
        self.btn_91.clicked.connect(self.question91)
        self.btn_92.clicked.connect(self.question92)
        self.btn_93.clicked.connect(self.question93)
        self.btn_94.clicked.connect(self.question94)
        self.btn_95.clicked.connect(self.question95)
        self.btn_96.clicked.connect(self.question96)
        self.btn_97.clicked.connect(self.question97)
        self.btn_98.clicked.connect(self.question98)
        self.btn_99.clicked.connect(self.question99)
        self.btn_100.clicked.connect(self.question100)
        self.btn_101.clicked.connect(self.question101)
        self.btn_102.clicked.connect(self.question102)


    def question1(self):
        global numberprompt_two
        numberprompt_two = 0
        global addressprompt_two
        addressprompt_two = 0
        self.question1 = TestPromptII()
        self.question1.show()

    def question2(self):
        global addressprompt_two
        addressprompt_two = 1
        global numberprompt_two
        numberprompt_two = 1
        self.question1 = TestPromptII()
        self.question1.show()

    def question3(self):
        global addressprompt_two
        addressprompt_two = 2
        global numberprompt_two
        numberprompt_two = 2
        self.question1 = TestPromptII()
        self.question1.show()

    def question4(self):
        global addressprompt_two
        addressprompt_two = 3
        global numberprompt_two
        numberprompt_two = 3
        self.question1 = TestPromptII()
        self.question1.show()

    def question5(self):
        global addressprompt_two
        addressprompt_two = 4
        global numberprompt_two
        numberprompt_two = 4
        self.question1 = TestPromptII()
        self.question1.show()

    def question6(self):
        global addressprompt_two
        addressprompt_two = 5
        global numberprompt_two
        numberprompt_two = 5
        self.question1 = TestPromptII()
        self.question1.show()

    def question7(self):
        global addressprompt_two
        addressprompt_two = 6
        global numberprompt_two
        numberprompt_two = 6
        self.question1 = TestPromptII()
        self.question1.show()

    def question8(self):
        global addressprompt_two
        addressprompt_two = 7
        global numberprompt_two
        numberprompt_two = 7
        self.question1 = TestPromptII()
        self.question1.show()

    def question9(self):
        global addressprompt_two
        addressprompt_two = 8
        global numberprompt_two
        numberprompt_two = 8
        self.question1 = TestPromptII()
        self.question1.show()

    def question10(self):
        global addressprompt_two
        addressprompt_two = 9
        global numberprompt_two
        numberprompt_two = 9
        self.question1 = TestPromptII()
        self.question1.show()

    def question11(self):
        global addressprompt_two
        addressprompt_two = 10
        global numberprompt_two
        numberprompt_two = 10
        self.question1 = TestPromptII()
        self.question1.show()

    def question12(self):
        global addressprompt_two
        addressprompt_two = 11
        global numberprompt_two
        numberprompt_two = 11
        self.question1 = TestPromptII()
        self.question1.show()

    def question13(self):
        global addressprompt_two
        addressprompt_two = 12
        global numberprompt_two
        numberprompt_two = 12
        self.question1 = TestPromptII()
        self.question1.show()

    def question14(self):
        global addressprompt_two
        addressprompt_two = 13
        global numberprompt_two
        numberprompt_two = 13
        self.question1 = TestPromptII()
        self.question1.show()

    def question15(self):
        global addressprompt_two
        addressprompt_two = 14
        global numberprompt_two
        numberprompt_two = 14
        self.question1 = TestPromptII()
        self.question1.show()

    def question16(self):
        global addressprompt_two
        addressprompt_two = 15
        global numberprompt_two
        numberprompt_two = 15
        self.question1 = TestPromptII()
        self.question1.show()

    def question17(self):
        global addressprompt_two
        addressprompt_two = 16
        global numberprompt_two
        numberprompt_two = 16
        self.question1 = TestPromptII()
        self.question1.show()

    def question18(self):
        global addressprompt_two
        addressprompt_two = 17
        global numberprompt_two
        numberprompt_two = 17
        self.question1 = TestPromptII()
        self.question1.show()

    def question19(self):
        global addressprompt_two
        addressprompt_two = 18
        global numberprompt_two
        numberprompt_two = 18
        self.question1 = TestPromptII()
        self.question1.show()

    def question20(self):
        global addressprompt_two
        addressprompt_two = 19
        global numberprompt_two
        numberprompt_two = 19
        self.question1 = TestPromptII()
        self.question1.show()

    def question21(self):
        global addressprompt_two
        addressprompt_two = 20
        global numberprompt_two
        numberprompt_two = 20
        self.question1 = TestPromptII()
        self.question1.show()

    def question22(self):
        global addressprompt_two
        addressprompt_two = 21
        global numberprompt_two
        numberprompt_two = 21
        self.question1 = TestPromptII()
        self.question1.show()

    def question23(self):
        global addressprompt_two
        addressprompt_two = 22
        global numberprompt_two
        numberprompt_two = 22
        self.question1 = TestPromptII()
        self.question1.show()

    def question24(self):
        global addressprompt_two
        addressprompt_two = 23
        global numberprompt_two
        numberprompt_two = 23
        self.question1 = TestPromptII()
        self.question1.show()

    def question25(self):
        global addressprompt_two
        addressprompt_two = 24
        global numberprompt_two
        numberprompt_two = 24
        self.question1 = TestPromptII()
        self.question1.show()

    def question26(self):
        global addressprompt_two
        addressprompt_two = 25
        global numberprompt_two
        numberprompt_two = 25
        self.question1 = TestPromptII()
        self.question1.show()

    def question27(self):
        global addressprompt_two
        addressprompt_two = 26
        global numberprompt_two
        numberprompt_two = 26
        self.question1 = TestPromptII()
        self.question1.show()

    def question28(self):
        global addressprompt_two
        addressprompt_two = 27
        global numberprompt_two
        numberprompt_two = 27
        self.question1 = TestPromptII()
        self.question1.show()

    def question29(self):
        global addressprompt_two
        addressprompt_two = 28
        global numberprompt_two
        numberprompt_two = 28
        self.question1 = TestPromptII()
        self.question1.show()

    def question30(self):
        global addressprompt_two
        addressprompt_two = 29
        global numberprompt_two
        numberprompt_two = 29
        self.question1 = TestPromptII()
        self.question1.show()

    def question31(self):
        global addressprompt_two
        addressprompt_two = 30
        global numberprompt_two
        numberprompt_two = 30
        self.question1 = TestPromptII()
        self.question1.show()

    def question32(self):
        global addressprompt_two
        addressprompt_two = 31
        global numberprompt_two
        numberprompt_two = 31
        self.question1 = TestPromptII()
        self.question1.show()

    def question33(self):
        global addressprompt_two
        addressprompt_two = 32
        global numberprompt_two
        numberprompt_two = 32
        self.question1 = TestPromptII()
        self.question1.show()

    def question34(self):
        global addressprompt_two
        addressprompt_two = 33
        global numberprompt_two
        numberprompt_two = 33
        self.question1 = TestPromptII()
        self.question1.show()

    def question35(self):
        global addressprompt_two
        addressprompt_two = 34
        global numberprompt_two
        numberprompt_two = 34
        self.question1 = TestPromptII()
        self.question1.show()

    def question36(self):
        global addressprompt_two
        addressprompt_two = 35
        global numberprompt_two
        numberprompt_two = 35
        self.question1 = TestPromptII()
        self.question1.show()

    def question37(self):
        global addressprompt_two
        addressprompt_two = 36
        global numberprompt_two
        numberprompt_two = 36
        self.question1 = TestPromptII()
        self.question1.show()

    def question38(self):
        global addressprompt_two
        addressprompt_two = 37
        global numberprompt_two
        numberprompt_two = 37
        self.question1 = TestPromptII()
        self.question1.show()

    def question39(self):
        global addressprompt_two
        addressprompt_two = 38
        global numberprompt_two
        numberprompt_two = 38
        self.question1 = TestPromptII()
        self.question1.show()

    def question40(self):
        global addressprompt_two
        addressprompt_two = 39
        global numberprompt_two
        numberprompt_two = 39
        self.question1 = TestPromptII()
        self.question1.show()

    def question41(self):
        global addressprompt_two
        addressprompt_two = 40
        global numberprompt_two
        numberprompt_two = 40
        self.question1 = TestPromptII()
        self.question1.show()

    def question42(self):
        global addressprompt_two
        addressprompt_two = 41
        global numberprompt_two
        numberprompt_two = 41
        self.question1 = TestPromptII()
        self.question1.show()

    def question43(self):
        global addressprompt_two
        addressprompt_two = 42
        global numberprompt_two
        numberprompt_two = 42
        self.question1 = TestPromptII()
        self.question1.show()

    def question44(self):
        global addressprompt_two
        addressprompt_two = 43
        global numberprompt_two
        numberprompt_two = 43
        self.question1 = TestPromptII()
        self.question1.show()

    def question45(self):
        global addressprompt_two
        addressprompt_two = 44
        global numberprompt_two
        numberprompt_two = 44
        self.question1 = TestPromptII()
        self.question1.show()

    def question46(self):
        global addressprompt_two
        addressprompt_two = 45
        global numberprompt_two
        numberprompt_two = 45
        self.question1 = TestPromptII()
        self.question1.show()

    def question47(self):
        global addressprompt_two
        addressprompt_two = 46
        global numberprompt_two
        numberprompt_two = 46
        self.question1 = TestPromptII()
        self.question1.show()

    def question48(self):
        global addressprompt_two
        addressprompt_two = 47
        global numberprompt_two
        numberprompt_two = 47
        self.question1 = TestPromptII()
        self.question1.show()

    def question49(self):
        global addressprompt_two
        addressprompt_two = 48
        global numberprompt_two
        numberprompt_two = 48
        self.question1 = TestPromptII()
        self.question1.show()

    def question50(self):
        global addressprompt_two
        addressprompt_two = 49
        global numberprompt_two
        numberprompt_two = 49
        self.question1 = TestPromptII()
        self.question1.show()

    def question51(self):
        global addressprompt_two
        addressprompt_two = 50
        global numberprompt_two
        numberprompt_two = 50
        self.question1 = TestPromptII()
        self.question1.show()

    def question52(self):
        global addressprompt_two
        addressprompt_two = 51
        global numberprompt_two
        numberprompt_two = 51
        self.question1 = TestPromptII()
        self.question1.show()

    def question53(self):
        global addressprompt_two
        addressprompt_two = 52
        global numberprompt_two
        numberprompt_two = 52
        self.question1 = TestPromptII()
        self.question1.show()

    def question54(self):
        global addressprompt_two
        addressprompt_two = 53
        global numberprompt_two
        numberprompt_two = 53
        self.question1 = TestPromptII()
        self.question1.show()

    def question55(self):
        global addressprompt_two
        addressprompt_two = 54
        global numberprompt_two
        numberprompt_two = 54
        self.question1 = TestPromptII()
        self.question1.show()

    def question56(self):
        global addressprompt_two
        addressprompt_two = 55
        global numberprompt_two
        numberprompt_two = 55
        self.question1 = TestPromptII()
        self.question1.show()

    def question57(self):
        global addressprompt_two
        addressprompt_two = 56
        global numberprompt_two
        numberprompt_two = 56
        self.question1 = TestPromptII()
        self.question1.show()

    def question58(self):
        global addressprompt_two
        addressprompt_two = 57
        global numberprompt_two
        numberprompt_two = 57
        self.question1 = TestPromptII()
        self.question1.show()

    def question59(self):
        global addressprompt_two
        addressprompt_two = 58
        global numberprompt_two
        numberprompt_two = 58
        self.question1 = TestPromptII()
        self.question1.show()

    def question60(self):
        global addressprompt_two
        addressprompt_two = 59
        global numberprompt_two
        numberprompt_two = 59
        self.question1 = TestPromptII()
        self.question1.show()

    def question61(self):
        global addressprompt_two
        addressprompt_two = 60
        global numberprompt_two
        numberprompt_two = 60
        self.question1 = TestPromptII()
        self.question1.show()

    def question62(self):
        global addressprompt_two
        addressprompt_two = 61
        global numberprompt_two
        numberprompt_two = 61
        self.question1 = TestPromptII()
        self.question1.show()

    def question63(self):
        global addressprompt_two
        addressprompt_two = 62
        global numberprompt_two
        numberprompt_two = 62
        self.question1 = TestPromptII()
        self.question1.show()

    def question64(self):
        global addressprompt_two
        addressprompt_two = 63
        global numberprompt_two
        numberprompt_two = 63
        self.question1 = TestPromptII()
        self.question1.show()

    def question65(self):
        global addressprompt_two
        addressprompt_two = 64
        global numberprompt_two
        numberprompt_two = 64
        self.question1 = TestPromptII()
        self.question1.show()

    def question66(self):
        global addressprompt_two
        addressprompt_two = 65
        global numberprompt_two
        numberprompt_two = 65
        self.question1 = TestPromptII()
        self.question1.show()

    def question67(self):
        global addressprompt_two
        addressprompt_two = 66
        global numberprompt_two
        numberprompt_two = 66
        self.question1 = TestPromptII()
        self.question1.show()

    def question68(self):
        global addressprompt_two
        addressprompt_two = 67
        global numberprompt_two
        numberprompt_two = 67
        self.question1 = TestPromptII()
        self.question1.show()

    def question69(self):
        global addressprompt_two
        addressprompt_two = 68
        global numberprompt_two
        numberprompt_two = 68
        self.question1 = TestPromptII()
        self.question1.show()

    def question70(self):
        global addressprompt_two
        addressprompt_two = 69
        global numberprompt_two
        numberprompt_two = 69
        self.question1 = TestPromptII()
        self.question1.show()

    def question71(self):
        global addressprompt_two
        addressprompt_two = 70
        global numberprompt_two
        numberprompt_two = 70
        self.question1 = TestPromptII()
        self.question1.show()

    def question72(self):
        global addressprompt_two
        addressprompt_two = 71
        global numberprompt_two
        numberprompt_two = 71
        self.question1 = TestPromptII()
        self.question1.show()

    def question73(self):
        global addressprompt_two
        addressprompt_two = 72
        global numberprompt_two
        numberprompt_two = 72
        self.question1 = TestPromptII()
        self.question1.show()

    def question74(self):
        global addressprompt_two
        addressprompt_two = 73
        global numberprompt_two
        numberprompt_two = 73
        self.question1 = TestPromptII()
        self.question1.show()

    def question75(self):
        global addressprompt_two
        addressprompt_two = 74
        global numberprompt_two
        numberprompt_two = 74
        self.question1 = TestPromptII()
        self.question1.show()

    def question76(self):
        global addressprompt_two
        addressprompt_two = 75
        global numberprompt_two
        numberprompt_two = 75
        self.question1 = TestPromptII()
        self.question1.show()

    def question77(self):
        global addressprompt_two
        addressprompt_two = 76
        global numberprompt_two
        numberprompt_two = 76
        self.question1 = TestPromptII()
        self.question1.show()

    def question78(self):
        global addressprompt_two
        addressprompt_two = 77
        global numberprompt_two
        numberprompt_two = 77
        self.question1 = TestPromptII()
        self.question1.show()

    def question79(self):
        global addressprompt_two
        addressprompt_two = 78
        global numberprompt_two
        numberprompt_two = 78
        self.question1 = TestPromptII()
        self.question1.show()

    def question80(self):
        global addressprompt_two
        addressprompt_two = 79
        global numberprompt_two
        numberprompt_two = 79
        self.question1 = TestPromptII()
        self.question1.show()

    def question81(self):
        global addressprompt_two
        addressprompt_two = 80
        global numberprompt_two
        numberprompt_two = 80
        self.question1 = TestPromptII()
        self.question1.show()

    def question82(self):
        global addressprompt_two
        addressprompt_two = 81
        global numberprompt_two
        numberprompt_two = 81
        self.question1 = TestPromptII()
        self.question1.show()

    def question83(self):
        global addressprompt_two
        addressprompt_two = 82
        global numberprompt_two
        numberprompt_two = 82
        self.question1 = TestPromptII()
        self.question1.show()

    def question84(self):
        global addressprompt_two
        addressprompt_two = 83
        global numberprompt_two
        numberprompt_two = 83
        self.question1 = TestPromptII()
        self.question1.show()

    def question85(self):
        global addressprompt_two
        addressprompt_two = 84
        global numberprompt_two
        numberprompt_two = 84
        self.question1 = TestPromptII()
        self.question1.show()

    def question86(self):
        global addressprompt_two
        addressprompt_two = 85
        global numberprompt_two
        numberprompt_two = 85
        self.question1 = TestPromptII()
        self.question1.show()

    def question87(self):
        global addressprompt_two
        addressprompt_two = 86
        global numberprompt_two
        numberprompt_two = 86
        self.question1 = TestPromptII()
        self.question1.show()

    def question88(self):
        global addressprompt_two
        addressprompt_two = 87
        global numberprompt_two
        numberprompt_two = 87
        self.question1 = TestPromptII()
        self.question1.show()

    def question89(self):
        global addressprompt_two
        addressprompt_two = 88
        global numberprompt_two
        numberprompt_two = 88
        self.question1 = TestPromptII()
        self.question1.show()

    def question90(self):
        global addressprompt_two
        addressprompt_two = 89
        global numberprompt_two
        numberprompt_two = 89
        self.question1 = TestPromptII()
        self.question1.show()

    def question91(self):
        global addressprompt_two
        addressprompt_two = 90
        global numberprompt_two
        numberprompt_two = 90
        self.question1 = TestPromptII()
        self.question1.show()

    def question92(self):
        global addressprompt_two
        addressprompt_two = 91
        global numberprompt_two
        numberprompt_two = 91
        self.question1 = TestPromptII()
        self.question1.show()

    def question93(self):
        global addressprompt_two
        addressprompt_two = 92
        global numberprompt_two
        numberprompt_two = 92
        self.question1 = TestPromptII()
        self.question1.show()

    def question94(self):
        global addressprompt_two
        addressprompt_two = 93
        global numberprompt_two
        numberprompt_two = 93
        self.question1 = TestPromptII()
        self.question1.show()

    def question95(self):
        global addressprompt_two
        addressprompt_two = 94
        global numberprompt_two
        numberprompt_two = 94
        self.question1 = TestPromptII()
        self.question1.show()

    def question96(self):
        global addressprompt_two
        addressprompt_two = 95
        global numberprompt_two
        numberprompt_two = 95
        self.question1 = TestPromptII()
        self.question1.show()

    def question97(self):
        global addressprompt_two
        addressprompt_two = 96
        global numberprompt_two
        numberprompt_two = 96
        self.question1 = TestPromptII()
        self.question1.show()

    def question98(self):
        global addressprompt_two
        addressprompt_two = 97
        global numberprompt_two
        numberprompt_two = 97
        self.question1 = TestPromptII()
        self.question1.show()

    def question99(self):
        global addressprompt_two
        addressprompt_two = 98
        global numberprompt_two
        numberprompt_two = 98
        self.question1 = TestPromptII()
        self.question1.show()

    def question100(self):
        global addressprompt_two
        addressprompt_two = 99
        global numberprompt_two
        numberprompt_two = 99
        self.question1 = TestPromptII()
        self.question1.show()

    def question101(self):
        global addressprompt_two
        addressprompt_two = 100
        global numberprompt_two
        numberprompt_two = 100
        self.question1 = TestPromptII()
        self.question1.show()

    def question102(self):
        global addressprompt_two
        addressprompt_two = 101
        global numberprompt_two
        numberprompt_two = 101
        self.question1 = TestPromptII()
        self.question1.show()

#список вопросов категории III
class QuestionsIII(QtWidgets.QMainWindow,Ui_QuestionsIIIWindow):
    def __init__(self):
        super(QuestionsIII, self).__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.question1)
        self.btn_2.clicked.connect(self.question2)
        self.btn_3.clicked.connect(self.question3)
        self.btn_4.clicked.connect(self.question4)
        self.btn_5.clicked.connect(self.question5)
        self.btn_6.clicked.connect(self.question6)
        self.btn_7.clicked.connect(self.question7)
        self.btn_8.clicked.connect(self.question8)
        self.btn_9.clicked.connect(self.question9)
        self.btn_10.clicked.connect(self.question10)
        self.btn_11.clicked.connect(self.question11)
        self.btn_12.clicked.connect(self.question12)
        self.btn_13.clicked.connect(self.question13)
        self.btn_14.clicked.connect(self.question14)
        self.btn_15.clicked.connect(self.question15)
        self.btn_16.clicked.connect(self.question16)
        self.btn_17.clicked.connect(self.question17)
        self.btn_18.clicked.connect(self.question18)
        self.btn_19.clicked.connect(self.question19)
        self.btn_20.clicked.connect(self.question20)
        self.btn_21.clicked.connect(self.question21)
        self.btn_22.clicked.connect(self.question22)
        self.btn_23.clicked.connect(self.question23)
        self.btn_24.clicked.connect(self.question24)
        self.btn_25.clicked.connect(self.question25)
        self.btn_26.clicked.connect(self.question26)
        self.btn_27.clicked.connect(self.question27)
        self.btn_28.clicked.connect(self.question28)
        self.btn_29.clicked.connect(self.question29)
        self.btn_30.clicked.connect(self.question30)
        self.btn_31.clicked.connect(self.question31)
        self.btn_32.clicked.connect(self.question32)
        self.btn_33.clicked.connect(self.question33)
        self.btn_34.clicked.connect(self.question34)
        self.btn_35.clicked.connect(self.question35)
        self.btn_36.clicked.connect(self.question36)
        self.btn_37.clicked.connect(self.question37)
        self.btn_38.clicked.connect(self.question38)
        self.btn_39.clicked.connect(self.question39)
        self.btn_40.clicked.connect(self.question40)
        self.btn_41.clicked.connect(self.question41)
        self.btn_42.clicked.connect(self.question42)
        self.btn_43.clicked.connect(self.question43)
        self.btn_44.clicked.connect(self.question44)
        self.btn_45.clicked.connect(self.question45)
        self.btn_46.clicked.connect(self.question46)
        self.btn_47.clicked.connect(self.question47)
        self.btn_48.clicked.connect(self.question48)
        self.btn_49.clicked.connect(self.question49)
        self.btn_50.clicked.connect(self.question50)
        self.btn_51.clicked.connect(self.question51)
        self.btn_52.clicked.connect(self.question52)
        self.btn_53.clicked.connect(self.question53)
        self.btn_54.clicked.connect(self.question54)
        self.btn_55.clicked.connect(self.question55)
        self.btn_56.clicked.connect(self.question56)
        self.btn_57.clicked.connect(self.question57)
        self.btn_58.clicked.connect(self.question58)
        self.btn_59.clicked.connect(self.question59)
        self.btn_60.clicked.connect(self.question60)

    def question1(self):
        global numberprompt_three
        numberprompt_three = 0
        global addressprompt_three
        addressprompt_three = 0
        self.question1 = TestPromptIII()
        self.question1.show()

    def question2(self):
        global addressprompt_three
        addressprompt_three = 1
        global numberprompt_three
        numberprompt_three = 1
        self.question1 = TestPromptIII()
        self.question1.show()

    def question3(self):
        global addressprompt_three
        addressprompt_three = 2
        global numberprompt_three
        numberprompt_three = 2
        self.question1 = TestPromptIII()
        self.question1.show()

    def question4(self):
        global addressprompt_three
        addressprompt_three = 3
        global numberprompt_three
        numberprompt_three = 3
        self.question1 = TestPromptIII()
        self.question1.show()

    def question5(self):
        global addressprompt_three
        addressprompt_three = 4
        global numberprompt_three
        numberprompt_three = 4
        self.question1 = TestPromptIII()
        self.question1.show()

    def question6(self):
        global addressprompt_three
        addressprompt_two = 5
        global numberprompt_three
        numberprompt_three = 5
        self.question1 = TestPromptIII()
        self.question1.show()

    def question7(self):
        global addressprompt_three
        addressprompt_three = 6
        global numberprompt_three
        numberprompt_three = 6
        self.question1 = TestPromptIII()
        self.question1.show()

    def question8(self):
        global addressprompt_three
        addressprompt_three = 7
        global numberprompt_three
        numberprompt_three = 7
        self.question1 = TestPromptIII()
        self.question1.show()

    def question9(self):
        global addressprompt_three
        addressprompt_three = 8
        global numberprompt_three
        numberprompt_three = 8
        self.question1 = TestPromptIII()
        self.question1.show()

    def question10(self):
        global addressprompt_three
        addressprompt_three = 9
        global numberprompt_three
        numberprompt_three = 9
        self.question1 = TestPromptIII()
        self.question1.show()

    def question11(self):
        global addressprompt_three
        addressprompt_three = 10
        global numberprompt_three
        numberprompt_three = 10
        self.question1 = TestPromptIII()
        self.question1.show()

    def question12(self):
        global addressprompt_three
        addressprompt_three = 11
        global numberprompt_three
        numberprompt_three = 11
        self.question1 = TestPromptIII()
        self.question1.show()

    def question13(self):
        global addressprompt_three
        addressprompt_three = 12
        global numberprompt_three
        numberprompt_three = 12
        self.question1 = TestPromptIII()
        self.question1.show()

    def question14(self):
        global addressprompt_three
        addressprompt_three = 13
        global numberprompt_three
        numberprompt_three = 13
        self.question1 = TestPromptIII()
        self.question1.show()

    def question15(self):
        global addressprompt_three
        addressprompt_three = 14
        global numberprompt_three
        numberprompt_three = 14
        self.question1 = TestPromptIII()
        self.question1.show()

    def question16(self):
        global addressprompt_three
        addressprompt_three = 15
        global numberprompt_three
        numberprompt_three = 15
        self.question1 = TestPromptIII()
        self.question1.show()

    def question17(self):
        global addressprompt_three
        addressprompt_three = 16
        global numberprompt_three
        numberprompt_three = 16
        self.question1 = TestPromptIII()
        self.question1.show()

    def question18(self):
        global addressprompt_three
        addressprompt_three = 17
        global numberprompt_three
        numberprompt_three = 17
        self.question1 = TestPromptIII()
        self.question1.show()

    def question19(self):
        global addressprompt_three
        addressprompt_three = 18
        global numberprompt_three
        numberprompt_three = 18
        self.question1 = TestPromptIII()
        self.question1.show()

    def question20(self):
        global addressprompt_three
        addressprompt_three = 19
        global numberprompt_three
        numberprompt_three = 19
        self.question1 = TestPromptIII()
        self.question1.show()

    def question21(self):
        global addressprompt_three
        addressprompt_three = 20
        global numberprompt_three
        numberprompt_three = 20
        self.question1 = TestPromptIII()
        self.question1.show()

    def question22(self):
        global addressprompt_three
        addressprompt_three = 21
        global numberprompt_three
        numberprompt_three = 21
        self.question1 = TestPromptIII()
        self.question1.show()

    def question23(self):
        global addressprompt_three
        addressprompt_three = 22
        global numberprompt_three
        numberprompt_three = 22
        self.question1 = TestPromptIII()
        self.question1.show()

    def question24(self):
        global addressprompt_three
        addressprompt_three = 23
        global numberprompt_three
        numberprompt_three = 23
        self.question1 = TestPromptIII()
        self.question1.show()

    def question25(self):
        global addressprompt_three
        addressprompt_three = 24
        global numberprompt_three
        numberprompt_three = 24
        self.question1 = TestPromptIII()
        self.question1.show()

    def question26(self):
        global addressprompt_three
        addressprompt_three = 25
        global numberprompt_three
        numberprompt_three = 25
        self.question1 = TestPromptIII()
        self.question1.show()

    def question27(self):
        global addressprompt_three
        addressprompt_three = 26
        global numberprompt_three
        numberprompt_three = 26
        self.question1 = TestPromptIII()
        self.question1.show()

    def question28(self):
        global addressprompt_three
        addressprompt_three = 27
        global numberprompt_three
        numberprompt_three = 27
        self.question1 = TestPromptIII()
        self.question1.show()

    def question29(self):
        global addressprompt_tthree
        addressprompt_three = 28
        global numberprompt_three
        numberprompt_three = 28
        self.question1 = TestPromptIII()
        self.question1.show()

    def question30(self):
        global addressprompt_three
        addressprompt_three = 29
        global numberprompt_three
        numberprompt_three = 29
        self.question1 = TestPromptIII()
        self.question1.show()

    def question31(self):
        global addressprompt_three
        addressprompt_three = 30
        global numberprompt_three
        numberprompt_three = 30
        self.question1 = TestPromptIII()
        self.question1.show()

    def question32(self):
        global addressprompt_three
        addressprompt_three = 31
        global numberprompt_three
        numberprompt_three = 31
        self.question1 = TestPromptIII()
        self.question1.show()

    def question33(self):
        global addressprompt_three
        addressprompt_three = 32
        global numberprompt_three
        numberprompt_three = 32
        self.question1 = TestPromptIII()
        self.question1.show()

    def question34(self):
        global addressprompt_three
        addressprompt_three = 33
        global numberprompt_three
        numberprompt_three = 33
        self.question1 = TestPromptIII()
        self.question1.show()

    def question35(self):
        global addressprompt_three
        addressprompt_three = 34
        global numberprompt_three
        numberprompt_three = 34
        self.question1 = TestPromptIII()
        self.question1.show()

    def question36(self):
        global addressprompt_three
        addressprompt_three = 35
        global numberprompt_three
        numberprompt_three = 35
        self.question1 = TestPromptIII()
        self.question1.show()

    def question37(self):
        global addressprompt_three
        addressprompt_three = 36
        global numberprompt_three
        numberprompt_three = 36
        self.question1 = TestPromptIII()
        self.question1.show()

    def question38(self):
        global addressprompt_three
        addressprompt_three = 37
        global numberprompt_three
        numberprompt_three = 37
        self.question1 = TestPromptIII()
        self.question1.show()

    def question39(self):
        global addressprompt_three
        addressprompt_three = 38
        global numberprompt_three
        numberprompt_three = 38
        self.question1 = TestPromptIII()
        self.question1.show()

    def question40(self):
        global addressprompt_three
        addressprompt_three = 39
        global numberprompt_three
        numberprompt_three = 39
        self.question1 = TestPromptIII()
        self.question1.show()

    def question41(self):
        global addressprompt_three
        addressprompt_three = 40
        global numberprompt_three
        numberprompt_three = 40
        self.question1 = TestPromptIII()
        self.question1.show()

    def question42(self):
        global addressprompt_three
        addressprompt_three = 41
        global numberprompt_three
        numberprompt_three = 41
        self.question1 = TestPromptIII()
        self.question1.show()

    def question43(self):
        global addressprompt_three
        addressprompt_three = 42
        global numberprompt_three
        numberprompt_three = 42
        self.question1 = TestPromptIII()
        self.question1.show()

    def question44(self):
        global addressprompt_three
        addressprompt_three = 43
        global numberprompt_three
        numberprompt_three = 43
        self.question1 = TestPromptIII()
        self.question1.show()

    def question45(self):
        global addressprompt_three
        addressprompt_three = 44
        global numberprompt_three
        numberprompt_three = 44
        self.question1 = TestPromptIII()
        self.question1.show()

    def question46(self):
        global addressprompt_three
        addressprompt_three = 45
        global numberprompt_three
        numberprompt_three = 45
        self.question1 = TestPromptIII()
        self.question1.show()

    def question47(self):
        global addressprompt_three
        addressprompt_three = 46
        global numberprompt_three
        numberprompt_three = 46
        self.question1 = TestPromptIII()
        self.question1.show()

    def question48(self):
        global addressprompt_three
        addressprompt_three = 47
        global numberprompt_three
        numberprompt_three = 47
        self.question1 = TestPromptIII()
        self.question1.show()

    def question49(self):
        global addressprompt_three
        addressprompt_three = 48
        global numberprompt_three
        numberprompt_three = 48
        self.question1 = TestPromptIII()
        self.question1.show()

    def question50(self):
        global addressprompt_three
        addressprompt_three = 49
        global numberprompt_three
        numberprompt_three = 49
        self.question1 = TestPromptIII()
        self.question1.show()

    def question51(self):
        global addressprompt_three
        addressprompt_three = 50
        global numberprompt_three
        numberprompt_three = 50
        self.question1 = TestPromptIII()
        self.question1.show()

    def question52(self):
        global addressprompt_three
        addressprompt_three = 51
        global numberprompt_three
        numberprompt_three = 51
        self.question1 = TestPromptIII()
        self.question1.show()

    def question53(self):
        global addressprompt_three
        addressprompt_three = 52
        global numberprompt_three
        numberprompt_three = 52
        self.question1 = TestPromptIII()
        self.question1.show()

    def question54(self):
        global addressprompt_three
        addressprompt_three = 53
        global numberprompt_three
        numberprompt_three = 53
        self.question1 = TestPromptIII()
        self.question1.show()

    def question55(self):
        global addressprompt_three
        addressprompt_three = 54
        global numberprompt_three
        numberprompt_three = 54
        self.question1 = TestPromptIII()
        self.question1.show()

    def question56(self):
        global addressprompt_three
        addressprompt_three = 55
        global numberprompt_three
        numberprompt_three = 55
        self.question1 = TestPromptIII()
        self.question1.show()

    def question57(self):
        global addressprompt_three
        addressprompt_three = 56
        global numberprompt_three
        numberprompt_three = 56
        self.question1 = TestPromptIII()
        self.question1.show()

    def question58(self):
        global addressprompt_three
        addressprompt_three = 57
        global numberprompt_three
        numberprompt_three = 57
        self.question1 = TestPromptIII()
        self.question1.show()

    def question59(self):
        global addressprompt_three
        addressprompt_three = 58
        global numberprompt_three
        numberprompt_three = 58
        self.question1 = TestPromptIII()
        self.question1.show()

    def question60(self):
        global addressprompt_three
        addressprompt_three = 59
        global numberprompt_three
        numberprompt_three = 59
        self.question1 = TestPromptIII()
        self.question1.show()

class Right(QtWidgets.QDialog,Ui_Right):
    def __init__(self):
        super(Right, self).__init__()
        self.setupUi(self)

class Wrong(QtWidgets.QDialog,Ui_Wrong):
    def __init__(self):
        super(Wrong, self).__init__()
        self.setupUi(self)

#список вопросов I
questionsI = ['Какая турбина установлена в блоке с прямоточным котлом ТГМП-314П?\nВыберите 1 правильный ответ:', #1
              'Как должен осуществляться контроль за общими расходами мазута и газа в котёл, за расходом питательной воды на каждый поток котла при пуске котла в работу?\nВыберите 2 правильных ответа:',#2
              'Укажите параметры пара, для выработки которого предназначен котел ТГМП-314П?\nВыберите 1 правильный ответ:', #3
              'На сжигание какого топлива рассчитан котельный агрегат ТГМП-314П?\nВыберите 1 правильный ответ:', #4
              'Укажите 1 верное утверждение:', #5
              'Укажите вид и количество воздухоподогревателей, установленных на котле:\nВыберите 1 правильный ответ:', #6
              'Какой способ очистки используется на РВП?\nВыберите 1 правильный ответ:', #7
              'Что входит в состав тягодутьевой установки котла?\nВыберите 2 неправильных ответа:', #8
              'Укажите 1 верное утверждение:', #9
              'Как обеспечивается крутка газо-воздушной смеси при подаче топлива в котел?\nВыберите 1 правильный ответ:', #10
              'При какой температуре окружающего воздуха обеспечивается крутка газо-воздушной смеси при подаче в котел?\nВыберите 1 правильный ответ:', #11
              'Укажите значение расхода мазута на горелку при номинальной нагрузке котла:\nВыберите 1 правильный ответ:', #12
              'Укажите значение расхода газа на горелку при номинальной нагрузке котла:\nВыберите 1 правильный ответ:', #13
              'Что применяется для сжигания мазута?\nВыберите 1 правильный ответ:', #14
              'Как может осуществляться питание котла?\nВыберите 2 правильных ответа:', #15
              'Укажите производительности турбонасоса 1100 т/ч при напоре  360 кгс/см^2 и электронасоса - 600 т/ч при 320 кгс/см^2:\nВыберите 1 правильный ответ:', #16
              'Сколько и какие потоки включает в себя паровой тракт?\nВыберите 1 правильный ответ:', #17
              'Как регулируется расход питательной воды на котел?\nВыберите 1 правильный ответ:', #18
              'Какие функции выполняет РПК?\nВыберите 1 правильный ответ:', #19
              'Значения температуры среды в одноименных сечениях поверхностей нагрева обоих потоков должны быть:\nВыберите 1 правильный ответ:', #20
              'Какие поверхности нагрева выполнены без перехода с одной стороны котла на другую выполнены без перехода с одной стороны котла на другую?\nВыберите 2 правильных ответа:', #21
              'Ниже приведена последовательность включения поверхностей нагрева по ходу среды в пароводяном тракте котла:\n1) водяной экономайзер (ВЭ);\n2) нижняя радиационная часть (НРЧ);\n3) подвесные трубы (ПТ);\n4) средняя радиационная часть (СРЧ);\n5) верхняя радиационная часть (ВРЧ);\n6) экраны поворотной камеры (ЭПК);\n7) потолочный экран (ПЭ);\n8) ширмы (ШПП);\n9) конвективный пароперегреватель (КПП в/д).\nУкажите 1 верное утверждение:', #22
              'Где расположена встроенная задвижка (ВЗ)?\nВыберите 1 правильный ответ:', #23
              'Как байпасируется встроенная задвижка (ВЗ)?\nВыберите 1 правильный ответ:', #24
              'Сколько ступеней промежуточного пароперегревателя и как они установлены?\nВыберите 1 правильный ответ:', #25
              'В каком диапазоне изменения нагрузки установленная на котле автоматика обеспечивает управление технологическими процессами?\nВыберите 1 правильный ответ:', #26
              'При каких значениях нагрузки котла температура промперегрева поддерживается равной номинальной?\nВыберите 1 правильный ответ:', #27
              'Каким соотношением осуществляется первичное регулирование температуры среды в пароводяном тракте котла?\nВыберите 1 правильный ответ:', #28
              'Как реализуется тонкое регулирование температуры в первичном тракте?\nВыберите 1 правильный ответ:', #29
              'Как расположены впрыски?\nВыберите 1 правильный ответ:', #30
              'Какие методы регулирования температуры пара промперегрева предусмотрены в данном котле?\nВыберите 2 правильных ответа:', #31
              'Где устанавливается аварийный впрыск?\nВыберите 1 правильный ответ:', #32
              'Где происходит отбор газов на рециркуляцию?\nВыберите 1 правильный ответ:', #33
              'Как поддерживается температура свежего и вторично перегретого пара во время растопок в пределах необходимых значений?\nВыберите 2 правильных ответа:', #34
              'Откуда подается вода на впрыск в пароохладители свежего пара и паропроводы вторично перегретого пара?\nВыберите 1 правильный ответ:', #35
              'Как подается питательная вода к котлу?\nВыберите 1 правильный ответ:', #36
              'Какой клапан установлен на питательном трубопроводе перед котлом?\nВыберите 1 правильный ответ:', #37
              'На что отбирается питательная вода перед обратным клапаном?\nВыберите 1 правильный ответ:', #38
              'Выберите 1 верное утверждение:',#39
              'Куда подается питательная вода через регулирующий клапан РПК?\nВыберите 1 правильный ответ:', #40
              'Укажите размер выходного коллектора экономайзера:\nВыберите 1 правильный ответ:', #41
              'Сколько всего змеевиков в НРЧ на один поток?\nВыберите 1 правильный ответ:', #42
              'Сколько частей НРЧ имеет данный котел?\nВыберите 1 правильный ответ:', #43
              'Куда поступает среда после НРЧ?\nВыберите 1 правильный ответ:', #44
              'Сколько труб входят в состав подвесных труб?\nВыберите 1 правильный ответ:', #45
              'Как поступает среда в выходные коллекторы, расположенные на потолке конвективной шахты?\nВыберите 1 правильный ответ:', #46
              'Откуда среда поступает в вертикальный смесительный коллектор?\nВыберите 1 правильный ответ:', #47
              'Как переходит среда из СРЧ в ВРЧ?\nВыберите 1 правильный ответ:', #48
              'Как конструктивно выполнены СРЧ-ВРЧ?\nВыберите 1 правильный ответ:', #49
              'Куда поступает среда после панелей СРЧ-ВРЧ?\nВыберите 1 правильный ответ:', #50
              'Где расположены экраны поворотной камеры, в которые поступает пар из смесительного коллектора 325х45, пройдя панели СРЧ-ВРЧ?\nВыберите 1 правильный ответ:', #51
              'Куда поступает среда из камеры экрана поворотной камеры, расположенных на фронтовой стене топки в верхней её части?\nВыберите 1 правильный ответ:', #52
              'Какое количество змеевиков экранизируют фронтовую и боковую стенки топки, а также боковую и заднюю стенки конвективной шахты?\nВыберите 1 правильный ответ:', #53
              'Где расположена встроенная задвижка (ВЗ) Ду-250?\nВыберите 1 правильный ответ:', #54
              'Где предусмотрен отвод среды на встроенные (пусковые) сепараторы?\nВыберите 1 правильный ответ:', #55
              'Как выполнен встроенный сепаратор?\nВыберите 1 правильный ответ:', #56
              'Как подводится среда во встроенный сепаратор?\nВыберите 1 правильный ответ:', #57
              'Как разделяются потоки во встроенном сепараторе после конического рассекателя и лопаток завихрителя?\nВыберите 2 правильных ответа:', #58
              'Когда разделяется поток во встроенном сепараторе?\nВыберите 2 правильных ответа:', #59
              'Где расположен пароохладитель (впрыск 1)?\nВыберите 1 правильный ответ:', #60
              'Чем образованы ШПП?\nВыберите 2 правильных ответа:', #61
              'Где расположен пароохладитель (впрыск 2)?\nВыберите 1 правильный ответ:', #62
              'Куда подается среда после впрыска 2?\nВыберите 1 правильный ответ:', #63
              'Какая схема соответствует движению среды в КПП?\nВыберите 1 правильный ответ:', #64
              'С какими параметрами пар подводится к цилиндру высокого давления (ЦВД) турбины после КПП?\nВыберите 1 правильный ответ:', #65
              'Где установлен пусковой впрыск?\nВыберите 1 правильный ответ:', #66
              'Что установлено на противоположных отводу пара на турбину торцах выходных коллекторов КПП?\nВыберите 2 правильных ответа:', #67
              'Где расположены главные паровые задвижки (ГПЗ)?\nВыберите 1 правильный ответ:', #68
              'Пар каких параметров подается в промежуточный пароперегреватель котла из ЦВД турбины?\nВыберите 1 правильный ответ:', #69
              'Какие клапаны установлены на двух "холодных" паропроводах, по которым пар подается в промежуточный пароперегреватель из ЦВД турбины?\nВыберите 1 правильный ответ:', #70
              'Что входит в состав КПП 1 ступени?\nВыберите 1 неправильный ответ:', #71
              'Где установлен аварийный впрыскивающий пароохладитель?\nВыберите 1 правильный ответ:', #72
              'Куда поступает пар по паропроводу после выходного коллектора перегревателя 2 ст.?\nВыберите 1 правильный ответ:', #73
              'Как расположены пакеты КПП в/д и КПП 2 ст. вторично перегретого пара?\nВыберите 1 правильный ответ:', #74
              'Где расположены входные и выходные коллекторы подвесных труб?\nВыберите 1 правильный ответ:', #75
              'Чем сопровождается действие защиты?\nВыберите 1 правильный ответ:', #76
              'Укажите 1 неверное утверждение:', #77
              'Как вводится в действие оборудование, отключенное защитой?\nВыберите 1 правильный ответ:', #78
              'Какие операции выполняют защиты котлоагрегата в зависимости от характера нарушения?\nВыберите 1 неправильный ответ:', #79
              'При каком значении давления природного газа после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:', #80
              'При каком значении давления мазута после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:', #81
              'Какое значение выдержки времени срабатывания защиты по понижению давления мазута после регулирующих клапанов предусмотрено при работе котла на мазуте?\nВыберите 1 правильный ответ:', #82
              'При достижении какого значения расхода питательной воды в котел срабатывает защита, осуществляющая аварийный останов котла?\nВыберите 1 правильный ответ:', #83
              'С какой выдержкой по времени действует защита по прекращению поступления питательной воды в котел?\nВыберите 1 правильный ответ:', #84
              'При каком значении давления природного газа перед горелками срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:', #85
              'При каком минимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ', #86
              'С какой выдержкой по времени действует защита по понижению давления среды перед встроенной задвижкой?\nВыберите 1 правильный ответ:', #87
              'При каком максимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:', #88
              'При понижении давления среды перед встроенной задвижкой во время пуска до какого значения предусмотрен аварийный останов котла защитами?\nВыберите 1 правильный ответ:', #89
              'При каких значениях расхода пара через промежуточный пароперегреватель предусмотрен аварийный останов защитой?\nВыберите 1 правильный ответ:', #90
              'С какой выдержкой по времени действует защита по понижению расхода пара через промежуточный пароперегреватель?\nВыберите 1 правильный ответ:', #91
              'Как измеряется расход пара через промежуточный пароперегреватель?\nВыберите 1 правильный ответ:', #92
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дымососов?\nВыберите 2 правильных ответа:', #93
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дутьевых вентиляторов?\nВыберите 2 правильных ответа:', #94
              'Когда предусмотрен аварийный останов защитами по останову РВП?\nВыберите 2 правильных ответа', #95
              'С какой выдержкой по времени предусмотрен аварийный останов при отключении обоих РВП?\nВыберите 1 правильный ответ:', #96
              'При каких условиях защита по понижению давления природного газа и мазута воздействует на останов котла?\nВыберите 1 неправильный ответ:', #97
              'В каких случаях предусматривается аварийный останов котла защитами?\nВыберите 2 неправильных ответа:', #98
              'Какие операции выполняются одновременно при останове котла защитой одновременно выполняются следующие операции?\nВыберите 2 неправильных ответа:', #99
              'Какие защиты, действующие на частичное снижение нагрузки блока, выполняются при наличии импульсной команды об отключении одного из механизмов?\nВыберите 1 неправильный ответ:', #100
              'С какой выдержкой времени выполняются команды об отключении одного из механизмов при действии защит по частичному снижению нагрузки блока?\nВыберите 1 правильный ответ:', #101
              'В каких случаях выполняются защиты по отключению одного из механизмов, предусматривающие частичное снижение нагрузки блока?\nВыберите 2 правильных ответа:', #102
              'С какой выдержкой времени действует защита по отключению ПТН и включению ПЭН системой АВР?\nВыберите 1 правильный ответ:', #103
              'При повышении температуры первичного пара перед турбиной до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:', #104
              'С какой выдержкой времени действует защита, предусматривающая частичное снижение нагрузки блока, при повышении температуры первичного пара перед турбиной?\nВыберите 1 правильный ответ:', #105
              'При повышении температуры вторичного пара на выходе из котла до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:', #106
              'С какой выдержкой времени действует защита, предусматривающая частичное снижение нагрузки котла, при повышении температуры вторичного пара на выходе из котла?\nВыберите 1 правильный ответ:', #107
              'Какая нагрузка задается котлу системой автоматического регулирования при срабатывании любой защиты, предусматривающей снижение нагрузки котла?\nВыберите 1 правильный ответ:', #108
              'В каких случаях производится частичное снижение нагрузки блока?\nВыберите 2 неправильных ответа:', #109
              'В каких случаях разрешается разгружение блока до 60% при срабатывании защит, действующих на снижение нагрузки блока?\nВыберите 1 правильный ответ:', #110
              'Как осуществляется контроль нагрузки при срабатывании защит, действующих на снижение нагрузки блока?\nВыберите 1 правильный ответ:', #111
              'Какие операций необходимо произвести при снижении нагрузки?\nВыберите 2 правильных ответа:', #112
              'Как вводятся и выводятся защиты, действующие на снижение нагрузки блока?\nВыберите 1 правильный ответ:', #113
              'При повышении давления острого пара в паропроводе перед ПСУ до первого предела, равного 1,05 РНОМ:\nВыберите 1 правильный ответ:', #114
              'При повышении давления острого пара за котлом в любом паропроводе до 2 предела равного 1,1 номинального:\nВыберите 1 правильный ответ:', #115
              'При каких условиях предусмотрена защита при повышении давления острого пара за котлом?\nВыберите 2 правильных ответа:', #116
              'Какие действия предусмотрены защитой при загорании отложений в РВП?\nВыберите 1 неправильный ответ:', #117
              'Как производится включение средств пожаротушения при загорании отложений в РВП?\nВыберите 1 правильный ответ:', #118
              'Какое значение является предельным при повышении температуры вторичного пара за котлом?\nВыберите 1 правильный ответ:', #119
              'Какие операции производятся при срабатывании защиты при повышении температуры вторичного пара выше предельного уровня?\nВыберите 1 правильный ответ:', #120
              'На каких горелках смонтирована и налажена защита по не воспламенению или погасанию факела?\nВыберите 2 правильных ответа:', #121
              'Как производится контроль наличия факела горелки во время розжига?\nВыберите 1 правильный вариант:', #122
              'Через какой промежуток времени срабатывает защита на отключение горелки при не воспламенении или погасании факела включаемой в работу растопочной горелки в процессе розжига?\nВыберите 1 правильный ответ:', #123
              'При повышении давления газа за регулирующим клапаном выше какого значения уставки срабатывает защита по понижению давления газа?\nВыберите 1 правильный ответ:', #124
              'Какими средствами измерения контролируется давлении газа за регулирующим клапаном?\nВыберите 1 правильный ответ:', #125
              'Когда выводится защита по понижению давления газа за   регулирующим клапаном?\nВыберите 2 правильных ответа:', #126
              'Когда разрешается розжиг горелок, не используемых при растопке котла?\nВыберите 1 правильный ответ:', #127
              'Когда снимается блокировка на запрет открытия задвижек и включение ЗЗУ на горелки, не входящих в растопочную группу?\nВыберите 1 правильный ответ:', #128
              'Кто производит опробование защит на "сигнал", в соответствии с графиком опробования защит энергоблоков?\nВыберите 1 правильный ответ:', #129
              ]

#список вопросов II
questionsII = ['Какая турбина установлена в блоке с прямоточным котлом ТГМП-314П?\nВыберите 1 правильный ответ:', #1
              'Как должен осуществляться контроль за общими расходами мазута и газа в котёл, за расходом питательной воды на каждый поток котла при пуске котла в работу?\nВыберите 2 правильных ответа:',#2
              'Укажите параметры пара, для выработки которого предназначен котел ТГМП-314П?\nВыберите 1 правильный ответ:', #3
              'На сжигание какого топлива рассчитан котельный агрегат ТГМП-314П?\nВыберите 1 правильный ответ:', #4
              'Укажите 1 верное утверждение:', #5
              'Укажите вид и количество воздухоподогревателей, установленных на котле:\nВыберите 1 правильный ответ:', #6
              'Что входит в состав тягодутьевой установки котла?\nВыберите 2 неправильных ответа:', #8
              'Укажите 1 верное утверждение:', #9
              'Как обеспечивается крутка газо-воздушной смеси при подаче топлива в котел?\nВыберите 1 правильный ответ:', #10
              'При какой температуре окружающего воздуха обеспечивается крутка газо-воздушной смеси при подаче в котел?\nВыберите 1 правильный ответ:', #11
              'Укажите значение расхода мазута на горелку при номинальной нагрузке котла:\nВыберите 1 правильный ответ:', #12
              'Укажите значение расхода газа на горелку при номинальной нагрузке котла:\nВыберите 1 правильный ответ:', #13
              'Как может осуществляться питание котла?\nВыберите 2 правильных ответа:', #15
              'Сколько и какие потоки включает в себя паровой тракт?\nВыберите 1 правильный ответ:', #17
              'Как регулируется расход питательной воды на котел?\nВыберите 1 правильный ответ:', #18
              'Какие функции выполняет РПК?\nВыберите 1 правильный ответ:', #19
              'Значения температуры среды в одноименных сечениях поверхностей нагрева обоих потоков должны быть:\nВыберите 1 правильный ответ:', #20
              'Какие поверхности нагрева выполнены без перехода с одной стороны котла на другую выполнены без перехода с одной стороны котла на другую?\nВыберите 2 правильных ответа:', #21
              'Ниже приведена последовательность включения поверхностей нагрева по ходу среды в пароводяном тракте котла:\n1) водяной экономайзер (ВЭ);\n2) нижняя радиационная часть (НРЧ);\n3) подвесные трубы (ПТ);\n4) средняя радиационная часть (СРЧ);\n5) верхняя радиационная часть (ВРЧ);\n6) экраны поворотной камеры (ЭПК);\n7) потолочный экран (ПЭ);\n8) ширмы (ШПП);\n9) конвективный пароперегреватель (КПП в/д).\nУкажите 1 верное утверждение:', #22
              'Где расположена встроенная задвижка (ВЗ)?\nВыберите 1 правильный ответ:', #23
              'Как байпасируется встроенная задвижка (ВЗ)?\nВыберите 1 правильный ответ:', #24
              'Сколько ступеней промежуточного пароперегревателя и как они установлены?\nВыберите 1 правильный ответ:', #25
              'При каких значениях нагрузки котла температура промперегрева поддерживается равной номинальной?\nВыберите 1 правильный ответ:', #27
              'Каким соотношением осуществляется первичное регулирование температуры среды в пароводяном тракте котла?\nВыберите 1 правильный ответ:', #28
              'Как реализуется тонкое регулирование температуры в первичном тракте?\nВыберите 1 правильный ответ:', #29
              'Как расположены впрыски?\nВыберите 1 правильный ответ:', #30
              'Какие методы регулирования температуры пара промперегрева предусмотрены в данном котле?\nВыберите 2 правильных ответа:', #31
              'Где устанавливается аварийный впрыск?\nВыберите 1 правильный ответ:', #32
              'Где происходит отбор газов на рециркуляцию?\nВыберите 1 правильный ответ:', #33
              'Как поддерживается температура свежего и вторично перегретого пара во время растопок в пределах необходимых значений?\nВыберите 2 правильных ответа:', #34
              'Откуда подается вода на впрыск в пароохладители свежего пара и паропроводы вторично перегретого пара?\nВыберите 1 правильный ответ:', #35
              'Какой клапан установлен на питательном трубопроводе перед котлом?\nВыберите 1 правильный ответ:', #37
              'На что отбирается питательная вода перед обратным клапаном?\nВыберите 1 правильный ответ:', #38
              'Выберите 1 верное утверждение:',#39
              'Куда подается питательная вода через регулирующий клапан РПК?\nВыберите 1 правильный ответ:', #40
              'Сколько частей НРЧ имеет данный котел?\nВыберите 1 правильный ответ:', #43
              'Куда поступает среда после НРЧ?\nВыберите 1 правильный ответ:', #44
              'Как переходит среда из СРЧ в ВРЧ?\nВыберите 1 правильный ответ:', #48
              'Где расположены экраны поворотной камеры, в которые поступает пар из смесительного коллектора 325х45, пройдя панели СРЧ-ВРЧ?\nВыберите 1 правильный ответ:', #51
              'Куда поступает среда из камеры экрана поворотной камеры, расположенных на фронтовой стене топки в верхней её части?\nВыберите 1 правильный ответ:', #52
              'Где расположена встроенная задвижка (ВЗ) Ду-250?\nВыберите 1 правильный ответ:', #54
              'Где предусмотрен отвод среды на встроенные (пусковые) сепараторы?\nВыберите 1 правильный ответ:', #55
              'Как выполнен встроенный сепаратор?\nВыберите 1 правильный ответ:', #56
              'Как подводится среда во встроенный сепаратор?\nВыберите 1 правильный ответ:', #57
              'Как разделяются потоки во встроенном сепараторе после конического рассекателя и лопаток завихрителя?\nВыберите 2 правильных ответа:', #58
              'Когда разделяется поток во встроенном сепараторе?\nВыберите 2 правильных ответа:', #59
              'Где расположен пароохладитель (впрыск 1)?\nВыберите 1 правильный ответ:', #60
              'Чем образованы ШПП?\nВыберите 2 правильных ответа:', #61
              'Где расположен пароохладитель (впрыск 2)?\nВыберите 1 правильный ответ:', #62
              'Куда подается среда после впрыска 2?\nВыберите 1 правильный ответ:', #63
              'Какая схема соответствует движению среды в КПП?\nВыберите 1 правильный ответ:', #64
              'С какими параметрами пар подводится к цилиндру высокого давления (ЦВД) турбины после КПП?\nВыберите 1 правильный ответ:', #65
              'Где установлен пусковой впрыск?\nВыберите 1 правильный ответ:', #66
              'Что установлено на противоположных отводу пара на турбину торцах выходных коллекторов КПП?\nВыберите 2 правильных ответа:', #67
              'Где расположены главные паровые задвижки (ГПЗ)?\nВыберите 1 правильный ответ:', #68
              'Пар каких параметров подается в промежуточный пароперегреватель котла из ЦВД турбины?\nВыберите 1 правильный ответ:', #69
              'Какие клапаны установлены на двух "холодных" паропроводах, по которым пар подается в промежуточный пароперегреватель из ЦВД турбины?\nВыберите 1 правильный ответ:', #70
              'Где установлен аварийный впрыскивающий пароохладитель?\nВыберите 1 правильный ответ:', #72
              'Куда поступает пар по паропроводу после выходного коллектора перегревателя 2 ст.?\nВыберите 1 правильный ответ:', #73
              'Как расположены пакеты КПП в/д и КПП 2 ст. вторично перегретого пара?\nВыберите 1 правильный ответ:', #74
              'Где расположены входные и выходные коллекторы подвесных труб?\nВыберите 1 правильный ответ:', #75
              'Чем сопровождается действие защиты?\nВыберите 1 правильный ответ:', #76
              'Укажите 1 неверное утверждение:', #77
              'Как вводится в действие оборудование, отключенное защитой?\nВыберите 1 правильный ответ:', #78
              'Какие операции выполняют защиты котлоагрегата в зависимости от характера нарушения?\nВыберите 1 неправильный ответ:', #79
              'При каком значении давления природного газа после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:', #80
              'При каком значении давления мазута после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:', #81
              'При достижении какого значения расхода питательной воды в котел срабатывает защита, осуществляющая аварийный останов котла?\nВыберите 1 правильный ответ:', #83
              'С какой выдержкой по времени действует защита по прекращению поступления питательной воды в котел?\nВыберите 1 правильный ответ:', #84
              'При каком значении давления природного газа перед горелками срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:', #85
              'При каком минимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ', #86
              'При каком максимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:', #88
              'При понижении давления среды перед встроенной задвижкой во время пуска до какого значения предусмотрен аварийный останов котла защитами?\nВыберите 1 правильный ответ:', #89
              'При каких значениях расхода пара через промежуточный пароперегреватель предусмотрен аварийный останов защитой?\nВыберите 1 правильный ответ:', #90
              'С какой выдержкой по времени действует защита по понижению расхода пара через промежуточный пароперегреватель?\nВыберите 1 правильный ответ:', #91
              'Как измеряется расход пара через промежуточный пароперегреватель?\nВыберите 1 правильный ответ:', #92
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дымососов?\nВыберите 2 правильных ответа:', #93
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дутьевых вентиляторов?\nВыберите 2 правильных ответа:', #94
              'Когда предусмотрен аварийный останов защитами по останову РВП?\nВыберите 2 правильных ответа', #95
              'С какой выдержкой по времени предусмотрен аварийный останов при отключении обоих РВП?\nВыберите 1 правильный ответ:', #96
              'При каких условиях защита по понижению давления природного газа и мазута воздействует на останов котла?\nВыберите 1 неправильный ответ:', #97
              'В каких случаях предусматривается аварийный останов котла защитами?\nВыберите 2 неправильных ответа:', #98
              'Какие операции выполняются одновременно при останове котла защитой одновременно выполняются следующие операции?\nВыберите 2 неправильных ответа:', #99
              'Какие защиты, действующие на частичное снижение нагрузки блока, выполняются при наличии импульсной команды об отключении одного из механизмов?\nВыберите 1 неправильный ответ:', #100
              'С какой выдержкой времени выполняются команды об отключении одного из механизмов при действии защит по частичному снижению нагрузки блока?\nВыберите 1 правильный ответ:', #101
              'С какой выдержкой времени действует защита по отключению ПТН и включению ПЭН системой АВР?\nВыберите 1 правильный ответ:', #103
              'При повышении температуры первичного пара перед турбиной до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:', #104
              'С какой выдержкой времени действует защита, предусматривающая частичное снижение нагрузки блока, при повышении температуры первичного пара перед турбиной?\nВыберите 1 правильный ответ:', #105
              'При повышении температуры вторичного пара на выходе из котла до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:', #106
              'С какой выдержкой времени действует защита, предусматривающая частичное снижение нагрузки котла, при повышении температуры вторичного пара на выходе из котла?\nВыберите 1 правильный ответ:', #107
              'Какая нагрузка задается котлу системой автоматического регулирования при срабатывании любой защиты, предусматривающей снижение нагрузки котла?\nВыберите 1 правильный ответ:', #108
              'В каких случаях производится частичное снижение нагрузки блока?\nВыберите 2 неправильных ответа:', #109
              'В каких случаях разрешается разгружение блока до 60% при срабатывании защит, действующих на снижение нагрузки блока?\nВыберите 1 правильный ответ:', #110
              'Как осуществляется контроль нагрузки при срабатывании защит, действующих на снижение нагрузки блока?\nВыберите 1 правильный ответ:', #111
              'Какие операций необходимо произвести при снижении нагрузки?\nВыберите 2 правильных ответа:', #112
              'При каких условиях предусмотрена защита при повышении давления острого пара за котлом?\nВыберите 2 правильных ответа:', #116
              'Какие действия предусмотрены защитой при загорании отложений в РВП?\nВыберите 1 неправильный ответ:', #117
              'Какое значение является предельным при повышении температуры вторичного пара за котлом?\nВыберите 1 правильный ответ:', #119
              'Как производится контроль наличия факела горелки во время розжига?\nВыберите 1 правильный вариант:', #122
              'При повышении давления газа за регулирующим клапаном выше какого значения уставки срабатывает защита по понижению давления газа?\nВыберите 1 правильный ответ:', #124
              'Какими средствами измерения контролируется давлении газа за регулирующим клапаном?\nВыберите 1 правильный ответ:', #125
              'Когда разрешается розжиг горелок, не используемых при растопке котла?\nВыберите 1 правильный ответ:', #127
              ]

#список вопросов III
questionsIII = ['Какая турбина установлена в блоке с прямоточным котлом ТГМП-314П?\nВыберите 1 правильный ответ:', #1
              'Укажите параметры пара, для выработки которого предназначен котел ТГМП-314П?\nВыберите 1 правильный ответ:', #3
              'На сжигание какого топлива рассчитан котельный агрегат ТГМП-314П?\nВыберите 1 правильный ответ:', #4
              'Укажите 1 верное утверждение:', #5
              'Укажите вид и количество воздухоподогревателей, установленных на котле:\nВыберите 1 правильный ответ:', #6
              'Что входит в состав тягодутьевой установки котла?\nВыберите 2 неправильных ответа:', #8
              'Укажите 1 верное утверждение:', #9
              'Как может осуществляться питание котла?\nВыберите 2 правильных ответа:', #15
              'Сколько и какие потоки включает в себя паровой тракт?\nВыберите 1 правильный ответ:', #17
              'Как регулируется расход питательной воды на котел?\nВыберите 1 правильный ответ:', #18
              'Какие функции выполняет РПК?\nВыберите 1 правильный ответ:', #19
              'Ниже приведена последовательность включения поверхностей нагрева по ходу среды в пароводяном тракте котла:\n1) водяной экономайзер (ВЭ);\n2) нижняя радиационная часть (НРЧ);\n3) подвесные трубы (ПТ);\n4) средняя радиационная часть (СРЧ);\n5) верхняя радиационная часть (ВРЧ);\n6) экраны поворотной камеры (ЭПК);\n7) потолочный экран (ПЭ);\n8) ширмы (ШПП);\n9) конвективный пароперегреватель (КПП в/д).\nУкажите 1 верное утверждение:', #22
              'Где расположена встроенная задвижка (ВЗ)?\nВыберите 1 правильный ответ:', #23
              'Сколько ступеней промежуточного пароперегревателя и как они установлены?\nВыберите 1 правильный ответ:', #25
              'В каком диапазоне изменения нагрузки установленная на котле автоматика обеспечивает управление технологическими процессами?\nВыберите 1 правильный ответ:', #26
              'При каких значениях нагрузки котла температура промперегрева поддерживается равной номинальной?\nВыберите 1 правильный ответ:', #27
              'Каким соотношением осуществляется первичное регулирование температуры среды в пароводяном тракте котла?\nВыберите 1 правильный ответ:', #28
              'Как реализуется тонкое регулирование температуры в первичном тракте?\nВыберите 1 правильный ответ:', #29
              'Как расположены впрыски?\nВыберите 1 правильный ответ:', #30
              'Какие методы регулирования температуры пара промперегрева предусмотрены в данном котле?\nВыберите 2 правильных ответа:', #31
              'Где происходит отбор газов на рециркуляцию?\nВыберите 1 правильный ответ:', #33
              'Откуда подается вода на впрыск в пароохладители свежего пара и паропроводы вторично перегретого пара?\nВыберите 1 правильный ответ:', #35
              'Какой клапан установлен на питательном трубопроводе перед котлом?\nВыберите 1 правильный ответ:', #37
              'На что отбирается питательная вода перед обратным клапаном?\nВыберите 1 правильный ответ:', #38
              'Где расположен пароохладитель (впрыск 1)?\nВыберите 1 правильный ответ:', #60
              'Где расположен пароохладитель (впрыск 2)?\nВыберите 1 правильный ответ:', #62
              'С какими параметрами пар подводится к цилиндру высокого давления (ЦВД) турбины после КПП?\nВыберите 1 правильный ответ:', #65
              'Где расположены главные паровые задвижки (ГПЗ)?\nВыберите 1 правильный ответ:', #68
              'Чем сопровождается действие защиты?\nВыберите 1 правильный ответ:', #76
              'Укажите 1 неверное утверждение:', #77
              'Какие операции выполняют защиты котлоагрегата в зависимости от характера нарушения?\nВыберите 1 неправильный ответ:', #79
              'При каком значении давления природного газа после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:', #80
              'При каком значении давления мазута после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:', #81
              'При достижении какого значения расхода питательной воды в котел срабатывает защита, осуществляющая аварийный останов котла?\nВыберите 1 правильный ответ:', #83
              'С какой выдержкой по времени действует защита по прекращению поступления питательной воды в котел?\nВыберите 1 правильный ответ:', #84
              'При каком значении давления природного газа перед горелками срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:', #85
              'При каком минимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ', #86
              'С какой выдержкой по времени действует защита по понижению давления среды перед встроенной задвижкой?\nВыберите 1 правильный ответ:', #87
              'При каком максимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:', #88
              'При понижении давления среды перед встроенной задвижкой во время пуска до какого значения предусмотрен аварийный останов котла защитами?\nВыберите 1 правильный ответ:', #89
              'При каких значениях расхода пара через промежуточный пароперегреватель предусмотрен аварийный останов защитой?\nВыберите 1 правильный ответ:', #90
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дымососов?\nВыберите 2 правильных ответа:', #93
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дутьевых вентиляторов?\nВыберите 2 правильных ответа:', #94
              'Когда предусмотрен аварийный останов защитами по останову РВП?\nВыберите 2 правильных ответа', #95
              'С какой выдержкой по времени предусмотрен аварийный останов при отключении обоих РВП?\nВыберите 1 правильный ответ:', #96
              'В каких случаях предусматривается аварийный останов котла защитами?\nВыберите 2 неправильных ответа:', #98
              'Какие защиты, действующие на частичное снижение нагрузки блока, выполняются при наличии импульсной команды об отключении одного из механизмов?\nВыберите 1 неправильный ответ:', #100
              'С какой выдержкой времени выполняются команды об отключении одного из механизмов при действии защит по частичному снижению нагрузки блока?\nВыберите 1 правильный ответ:', #101
              'В каких случаях выполняются защиты по отключению одного из механизмов, предусматривающие частичное снижение нагрузки блока?\nВыберите 2 правильных ответа:', #102
              'С какой выдержкой времени действует защита по отключению ПТН и включению ПЭН системой АВР?\nВыберите 1 правильный ответ:', #103
              'При повышении температуры первичного пара перед турбиной до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:', #104
              'При повышении температуры вторичного пара на выходе из котла до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:', #106
              'Какая нагрузка задается котлу системой автоматического регулирования при срабатывании любой защиты, предусматривающей снижение нагрузки котла?\nВыберите 1 правильный ответ:', #108
              'В каких случаях производится частичное снижение нагрузки блока?\nВыберите 2 неправильных ответа:', #109
              'При каких условиях предусмотрена защита при повышении давления острого пара за котлом?\nВыберите 2 правильных ответа:', #116
              'Как производится включение средств пожаротушения при загорании отложений в РВП?\nВыберите 1 правильный ответ:', #118
              'Какое значение является предельным при повышении температуры вторичного пара за котлом?\nВыберите 1 правильный ответ:', #119
              'Через какой промежуток времени срабатывает защита на отключение горелки при не воспламенении или погасании факела включаемой в работу растопочной горелки в процессе розжига?\nВыберите 1 правильный ответ:', #123
              'При повышении давления газа за регулирующим клапаном выше какого значения уставки срабатывает защита по понижению давления газа?\nВыберите 1 правильный ответ:', #124
              'Кто производит опробование защит на "сигнал", в соответствии с графиком опробования защит энергоблоков?\nВыберите 1 правильный ответ:', #129
              ]

#словарь вопрос-ответ
question_answer={'Какая турбина установлена в блоке с прямоточным котлом ТГМП-314П?\nВыберите 1 правильный ответ:':['Т-250/300-240','Т-110/120-130' ,'ПТ-135/162-130','К-300-240'], #1
              'Как должен осуществляться контроль за общими расходами мазута и газа в котёл, за расходом питательной воды на каждый поток котла при пуске котла в работу?\nВыберите 2 правильных ответа:':['по растопочным расходомерам','датчиками на пониженный перепад давления','датчиками абсолютного давления','датчиками гидростатического давления'],#2
              'Укажите параметры пара, для выработки которого предназначен котел ТГМП-314П?\nВыберите 1 правильный ответ:':['пар сверхкритического давления с температурой перегрева 545°С','пар высокого давления с температурой перегрева 450°С','пар сверхкритического давления с температурой перегрева 454°С','пар высокого давления с температурой перегрева 545°С'], #3
              'На сжигание какого топлива рассчитан котельный агрегат ТГМП-314П?\nВыберите 1 правильный ответ:':['природного газа и мазута','мазута и твердого топлива','твердого топлива и природного газа','только твердого топлива'], #4
              'Укажите 1 верное утверждение:':['ТГМП-314П - котельный агрегат прямоточный,\n с П-образной однокорпусной компоновкой','ТГМП-314П - котельный агрегат однобарабанный,\n вертикально-водотрубный, с естественной циркуляцией','ТГМП-314П - котельный агрегат однобарабанный,\n вертикально-водотрубный, с принудительной циркуляцией','ТГМП-314П - котельный агрегат прямоточный,\n с Т-образной однокорпусной компоновкой'], #5
              'Укажите вид и количество воздухоподогревателей, установленных на котле:\nВыберите 1 правильный ответ:':['2 регенеративных воздухоподогревателя','2 рекуперативных воздухоподогревателя','1 регенеративный, 1 рекуперативный воздухоподогреватели','1 регенеративный воздухоподогреватель'], #6
              'Какой способ очистки используется на РВП?\nВыберите 1 правильный ответ:':['газо-импульсная термоволновая очистка','паровая обдувка','дробеочистка','вибрационная очистка'], #7
              'Что входит в состав тягодутьевой установки котла?\nВыберите 2 неправильных ответа:':['два дутьевых вентилятора ВД-2,8 одностороннего всасывания','два дымососа рециркуляции дымовых газов одностороннего всасывания типа ДРГ-25','два дымососа типа ДОД-31,5 ФГМ','два дутьевых вентилятора типа ВДН-25х2 двухстороннего всасывания'], #8
              'Укажите 1 верное утверждение:':['в качестве горелочных устройств использованы газо-мазутные горелки,\n расположенные вертикально в два ряда в поду топочной камеры','в качестве горелочных устройств использованы пылегазовые горелки,\n расположенные вертикально в три ряда в поду топочной камеры','в качестве горелочных устройств использованы газо-мазутные горелки,\n расположенные встречно-смещенно на фронтальной и задней стенках','в качестве горелочных устройств использованы газо-мазутные горелки,\n применяется угловое расположение в два ряда'], #9
              'Как обеспечивается крутка газо-воздушной смеси при подаче топлива в котел?\nВыберите 1 правильный ответ:':['на периферийном и центральнном каналах установлены завихрители','на одном из каналов установлен завихритель','с помощью газовой форсунки','за счет сжатия и расширения газо-воздушной смеси'], #10
              'При какой температуре окружающего воздуха обеспечивается крутка газо-воздушной смеси при подаче в котел?\nВыберите 1 правильный ответ:':['в диапазоне от минус 30°С (с использованием рециркуляции подогретого воздуха)\n до плюс 45°С','в диапазоне от минус 30°С до плюс 45°С','в диапазоне от минус 45°С до плюс 30°С','в диапазоне от минус 30°С (с использованием рециркуляции подогретого воздуха)\n до плюс 20°С'], #11
              'Укажите значение расхода мазута на горелку при номинальной нагрузке котла:\nВыберите 1 правильный ответ:':['8,9 т/ч','10,5*10^3 нм^3/c','8,9*10^3 нм^3/ч','10,5 т/ч'], #12
              'Укажите значение расхода газа на горелку при номинальной нагрузке котла:\nВыберите 1 правильный ответ:':['10,5*10^3 нм^3/ч','15,6*10^3 нм^3/ч','10,5*10^3 нм^3/с','8,9*103 нм^3/ч'], #13
              'Что применяется для сжигания мазута?\nВыберите 1 правильный ответ:':['паромеханические форсунки типа "Эдипол"','электрогидравлические форсунки Bosch','пьезоэлектрические форсунки Siemens','электромагнитные форсунки типа Bosch Common Rail'], #14
              'Как может осуществляться питание котла?\nВыберите 2 правильных ответа:':['турбонасосом','пускорезервным электронасосом','паровым инжектором','насосом с ручным приводом'], #15
              'Укажите производительности турбонасоса 1100 т/ч при напоре  360 кгс/см^2 и электронасоса - 600 т/ч при 320 кгс/см^2:\nВыберите 1 правильный ответ:':['турбонасос - 1100 т/ч, электронасос - 600 т/ч','турбонасос - 600 т/ч, электронасос - 1100 т/ч','турбонасос – 550 т/ч, электронасос - 1050 т/ч','турбонасос - 1050 т/ч, электронасос - 700 т/ч'], #16
              'Сколько и какие потоки включает в себя паровой тракт?\nВыберите 1 правильный ответ:':['два несмешиваемых потока','два смешиваемых потока','четыре несмешиваемых потока','четыре смешиваемых потока'], #17
              'Как регулируется расход питательной воды на котел?\nВыберите 1 правильный ответ:':['питательным насосом','сетевым насосом','циркуляционным насосом','подогревателем высокого давления'], #18
              'Какие функции выполняет РПК?\nВыберите 1 правильный ответ:':['распределение питательной воды по потокам','регулирование расхода топлива','регулирование давления пара','регулирование подачи воздуха'], #19
              'Значения температуры среды в одноименных сечениях поверхностей нагрева обоих потоков должны быть:\nВыберите 1 правильный ответ:':['одинаковыми','отличаться на 20 ºС','отличаться на 10 ºС','отличаться на 5 ºС'], #20
              'Какие поверхности нагрева выполнены без перехода с одной стороны котла на другую выполнены без перехода с одной стороны котла на другую?\nВыберите 2 правильных ответа:':['экраны поворотной камеры','ширмы','нижняя радиационная часть','экономайзер'], #21
              'Ниже приведена последовательность включения поверхностей нагрева по ходу среды в пароводяном тракте котла:\n1) водяной экономайзер (ВЭ);\n2) нижняя радиационная часть (НРЧ);\n3) подвесные трубы (ПТ);\n4) средняя радиационная часть (СРЧ);\n5) верхняя радиационная часть (ВРЧ);\n6) экраны поворотной камеры (ЭПК);\n7) потолочный экран (ПЭ);\n8) ширмы (ШПП);\n9) конвективный пароперегреватель (КПП в/д).\nУкажите 1 верное утверждение:':['приведенная последовательность включения поверхностей нагрева по ходу среды\n в пароводяном тракте котла является правильной','водяной экономайзер (ВЭ) не входит в состав пароводяного тракта', 'подвесные трубы (ПТ) расположены после верхней радиационной части (ВРЧ)','конвективный пароперегреватель (КПП в/д) расположен перед потолочным экраном (ПЭ)'], #22
              'Где расположена встроенная задвижка (ВЗ)?\nВыберите 1 правильный ответ:':['на трубопроводе между ПЭ и ШПП','на трубопроводе между ЭПК и ПЭ','на трубопроводе между ВРЧ и ЭПК','на трубопроводе между ЭПК и ПЭ'], #23
              'Как байпасируется встроенная задвижка (ВЗ)?\nВыберите 1 правильный ответ:':['встроенными сепараторами с соответствующей дроссельной арматурой','циркуляционным насосом','шиберной задвижкой с трубопроводом','двумя предохранительными клапанами с трубопроводом'], #24
              'Сколько ступеней промежуточного пароперегревателя и как они установлены?\nВыберите 1 правильный ответ:':['по ходу пара в каждом потоке последовательно установлено\n две ступени пароперегревателя','по ходу пара в каждом потоке параллельно установлено\n две ступени пароперегревателя','по ходу пара в каждом потоке последовательно установлено\n три ступени пароперегревателя','по ходу пара в каждом потоке параллельно установлено\n три ступени пароперегревателя'], #25
              'В каком диапазоне изменения нагрузки установленная на котле автоматика обеспечивает управление технологическими процессами?\nВыберите 1 правильный ответ:':['от 30 до 100%','от 40 до 100%','от 60 до 100%','от 55 до 100%'], #26
              'При каких значениях нагрузки котла температура промперегрева поддерживается равной номинальной?\nВыберите 1 правильный ответ:':['от 50 до 100%','от 40 до 100%','от 70 до 100%','от 80 до 100%'], #27
              'Каким соотношением осуществляется первичное регулирование температуры среды в пароводяном тракте котла?\nВыберите 1 правильный ответ:':['"топливо-вода"','"топливо-воздух"','"вода-пар"','"вода-воздух"'], #28
              'Как реализуется тонкое регулирование температуры в первичном тракте?\nВыберите 1 правильный ответ:':['с помощью двух впрысков','с помощью поверхностного пароохладителя','с помощью трех впрысков','с помощью двух поверхностных пароохладителя,\n включенных последовательно'], #29
              'Как расположены впрыски?\nВыберите 1 правильный ответ:':['первый впрыск - перед ширмовым пароперегревателем,\n второй - перед конвективным пароперегревателем','первый впрыск - перед конвективным пароперегревателем,\n второй - перед ширмовым пароперегревателем','оба впрыска – перед конвективным пароперегревателем','оба впрыска – перед ширмовым пароперегревателем'], #30
              'Какие методы регулирования температуры пара промперегрева предусмотрены в данном котле?\nВыберите 2 правильных ответа:':['рециркуляция дымовых газов','аварийный впрыск','байпасирование части пара меньшей температуры','паровые теплообменники'], #31
              'Где устанавливается аварийный впрыск?\nВыберите 1 правильный ответ:':['перед 2-й ступенью пароперегревателя','перед 1-й ступенью пароперегревателя','перед 1-й и 2-й ступенью пароперегревателя','после пароперегревателя'], #32
              'Где происходит отбор газов на рециркуляцию?\nВыберите 1 правильный ответ:':['за ВЭ','перед КПП','перед ШПП','после ПЭ'], #33
              'Как поддерживается температура свежего и вторично перегретого пара во время растопок в пределах необходимых значений?\nВыберите 2 правильных ответа:':['пусковыми впрысками в паропроводы','паровыми байпасами промперегревателя','поверхностными теплообменниками','рециркуляцией газов'], #34
              'Откуда подается вода на впрыск в пароохладители свежего пара и паропроводы вторично перегретого пара?\nВыберите 1 правильный ответ:':['вода на впрыск в пароохладители свежего пара подается из питательного трубопровода,\n а в паропроводы вторично перегретого пара из промступеней питательных насосов','вода на впрыск в пароохладители свежего пара подается из водяного экономайзера,\n а в паропроводы вторично перегретого пара из промступеней питательных насосов','вода на впрыск в пароохладители свежего пара и в паропроводы вторично перегретого пара\n подается из водяного экономайзера','вода на впрыск в пароохладители свежего пара и в паропроводы вторично перегретого пара\n подается из промступеней питательных насосов'], #35
              'Как подается питательная вода к котлу?\nВыберите 1 правильный ответ:':['одним трубопроводом  377х45 ст. 15 ГС','двумя трубопроводами 325х50 ст. 12Х1МФ','двумя трубопроводами 325х40 ст. 15ГС','одним трубопроводом  159х20 ст. 20 ГС'], #36
              'Какой клапан установлен на питательном трубопроводе перед котлом?\nВыберите 1 правильный ответ:':['обратный клапан','регулирующий клапан','запорный клапан','предохранительный клапан'], #37
              'На что отбирается питательная вода перед обратным клапаном?\nВыберите 1 правильный ответ:':['на впрыски в паровой тракт котла','на подогреватели высокого давления','на деаэратор','на подогреватели низкого давления'], #38
              'Выберите 1 верное утверждение:':['за обратным клапаном питательный трубопровод разделяется на две нитки "А" и "Б",\n каждая из которых становится самостоятельно регулируемым потоком','нитки "А" и "Б" питательного трубопровода включают в себя разные поверхности нагрева','питательная вода на впрыски в паровой тракт котла отбирается после обратного клапана','за обратным клапаном питательный трубопровод не разделяется на две нити'],#39
              'Куда подается питательная вода через регулирующий клапан РПК?\nВыберите 1 правильный ответ:':['во входной коллектор водяного экономайзера','во входной коллектор НРЧ','во входной коллектор подвесных труб','в ШПП 1 ст.'], #40
              'Укажите размер выходного коллектора экономайзера:\nВыберите 1 правильный ответ:':['273х40','159х20','377х45','325х40'], #41
              'Сколько всего змеевиков в НРЧ на один поток?\nВыберите 1 правильный ответ:':['123','41','82','61'], #42
              'Сколько частей НРЧ имеет данный котел?\nВыберите 1 правильный ответ:':['2','1','3','4'], #43
              'Куда поступает среда после НРЧ?\nВыберите 1 правильный ответ:':['во входной коллектор подвесных труб','в вертикальный смесительный коллектор','во входной коллектор СРЧ-ВРЧ','в собирающий коллектор'], #44
              'Сколько труб входят в состав подвесных труб?\nВыберите 1 правильный ответ:':['159','82','53','171'], #45
              'Как поступает среда в выходные коллекторы, расположенные на потолке конвективной шахты?\nВыберите 1 правильный ответ:':['тремя лентами (по 53 трубы)','по шести трубам 159х18','девятью трубами 133х15','четырьмя трубами 159х20 ст. 20'], #46
              'Откуда среда поступает в вертикальный смесительный коллектор?\nВыберите 1 правильный ответ:':['после выходных коллекторов 219х36, расположенных на потолке конвективной шахты','после выходных коллекторов НРЧ 219х36','после входных коллекторов СРЧ-ВРЧ 159х28','после вертикальных камер 219х32 экрана поворотной камеры'], #47
              'Как переходит среда из СРЧ в ВРЧ?\nВыберите 1 правильный ответ:':['без разделительных коллекторов, деление поверхности нагрева на СРЧ и ВРЧ условное','по шести трубам 159х18','по 247 змеевикам 38х6','по трубопроводу 219х30'], #48
              'Как конструктивно выполнены СРЧ-ВРЧ?\nВыберите 1 правильный ответ:':['из 9 панелей, каждая из которых образована 23 змеевиками из труб 32х6','из 3-х панелей, каждая из которых образована 41 змеевиком из труб 36х6','тремя лентами (по 53 трубы)','из 221 змеевиков  32x6 ст. Х18Н12Т'], #49
              'Куда поступает среда после панелей СРЧ-ВРЧ?\nВыберите 1 правильный ответ:':['в 9 выходных коллекторов 159х28','в вертикальный смесительный коллектор 325х45 ("паук")',' в 3 входных камеры 219х36 потолочного экрана','в 6 выходных коллекторов 219х36, расположенных на потолке конвективной шахты'], #50
              'Где расположены экраны поворотной камеры, в которые поступает пар из смесительного коллектора 325х45, пройдя панели СРЧ-ВРЧ?\nВыберите 1 правильный ответ:':['на фронтовой стене топки в верхней её части','в газоходе котла','в не обогреваемой зоне у боковой стены конвективной шахты','на подвесных трубах'], #51
              'Куда поступает среда из камеры экрана поворотной камеры, расположенных на фронтовой стене топки в верхней её части?\nВыберите 1 правильный ответ:':['в 3 выходные камеры экрана поворотной камеры, а затем в 3 входные камеры потолочного экрана','в 3 выходные камеры потолочного экрана, а затем во входные коллекторы СРЧ-ВРЧ','в 3 входных коллектора, расположенных над потолком топки, а затем в ШПП 1 ст.','в выходные коллекторы ВРЧ, а затем в 3 входные камеры потолочного экрана'], #52
              'Какое количество змеевиков экранизируют фронтовую и боковую стенки топки, а также боковую и заднюю стенки конвективной шахты?\nВыберите 1 правильный ответ:':['180 змеевиков 38х6','247 змеевиков 36х6','207 змеевиков 32х6','123 змеевиков 36х6'], #53
              'Где расположена встроенная задвижка (ВЗ) Ду-250?\nВыберите 1 правильный ответ:':['врезана в смесительный коллектор 325х45, расположенный в конвективной шахте','врезана в коллектор 273х40,\n расположенный в газоходе котла','врезана в собирающий коллектор 219х32,\n расположенный в НРЧ','врезана в вертикальные камеры 219х32 экрана поворотной камеры,\n расположенных на фронтовой стене топки'], #54
              'Где предусмотрен отвод среды на встроенные (пусковые) сепараторы?\nВыберите 1 правильный ответ:':['перед ВЗ','перед СРЧ-ВРЧ','после экономайзера','после ШПП 2 ст'], #55
              'Как выполнен встроенный сепаратор?\nВыберите 1 правильный ответ:':['в виде вертикальной трубы 377х60','в виде 4 змеевиков 32х6','в виде 9 труб 133х15','в виде коллектора 273х40'], #56
              'Как подводится среда во встроенный сепаратор?\nВыберите 1 правильный ответ:':['в верхнее донышко, осевой подвод','в завихритель, радиальный подвод','в криволинейные каналы, осевой подвод','в патрубок подвода среды, радиальный подвод'], #57
              'Как разделяются потоки во встроенном сепараторе после конического рассекателя и лопаток завихрителя?\nВыберите 2 правильных ответа:':['вода отбрасывается к наружным стенкам и через горизонтальный\n штуцер направляется в растопочный расширитель','пар - через диффузор в нижнем донышке по трубопроводу - в коллектор,\n на котором установлен пароохладитель (впрыск 1), а из него подводится к ШПП 1 ст.','вода через коллектор, на котором установлен\n пароохладитель (впрыск 2), подводится к ШПП 2 ст','пароводяная смесь отбрасывается к наружным стенкам и\n через горизонтальный штуцер направляется в растопочный расширитель'], #58
              'Когда разделяется поток во встроенном сепараторе?\nВыберите 2 правильных ответа:':['после конического рассекателя','после лопаток завихрителя','после ШПП 1 ст.','после растопочного расширителя'], #59
              'Где расположен пароохладитель (впрыск 1)?\nВыберите 1 правильный ответ:':['на коллекторе за встроенной задвижкой перед ШПП 1 ст.','перед растопочным расширителем','на выходном коллекторе ШПП 2 ст.','после ШПП 1 ст.'], #60
              'Чем образованы ШПП?\nВыберите 2 правильных ответа:':['входным и выходным коллектором 155х28','24-я U-образными змеевиками 32х6','десятью трубами 106х14','32-я змеевикам 38х6 в виде спиральной трубы'], #61
              'Где расположен пароохладитель (впрыск 2)?\nВыберите 1 правильный ответ:':['на выходном коллекторе ШПП 2 ст.','на выходном коллекторе ШПП 1 ст.','на входном коллекторе ШПП 1 ст.','на входном коллекторе ШПП 2 ст.'], #62
              'Куда подается среда после впрыска 2?\nВыберите 1 правильный ответ:':['в конвективный пароперегреватель','в ширмовый пароперегреватель','в цилиндр высокого давления турбины','в предохранительные клапаны'], #63
              'Какая схема соответствует движению среды в КПП?\nВыберите 1 правильный ответ:':['прямоточная','противоточная','последовательно- смешанная','параллельно-смешанная'], #64
              'С какими параметрами пар подводится к цилиндру высокого давления (ЦВД) турбины после КПП?\nВыберите 1 правильный ответ:':['с температурой 545 °С и давлением 255 кг/см^2','с температурой 450 °С и давлением 234 кг/см^2','с температурой 635 °С и давлением 267 кг/см^2','с температурой 370 °С и давлением 210 кг/см^2'], #65
              'Где установлен пусковой впрыск?\nВыберите 1 правильный ответ:':['за котлом на главном трубопроводе','на выходном коллекторе ШПП 1 ст.','на входном коллекторе КПП','после ВРЧ'], #66
              'Что установлено на противоположных отводу пара на турбину торцах выходных коллекторов КПП?\nВыберите 2 правильных ответа:':['четыре главных предохранительных клапана Ду-125','четыре импульсных клапана Ду-20','четыре дроссельных клапана Ду-100','регулирующий клапан РПК'], #67
              'Где расположены главные паровые задвижки (ГПЗ)?\nВыберите 1 правильный ответ:':['перед стопорными клапанами турбины','после предохранительных клапанов, установленных на выходных коллекторах КПП','на питательном трубопроводе перед котлом','после РПК'], #68
              'Пар каких параметров подается в промежуточный пароперегреватель котла из ЦВД турбины?\nВыберите 1 правильный ответ:':['температурой 297 °С и давлением 40,3 кгс/см^2','температурой 450 °С и давлением 87 кгс/см^2','температурой 120 °С и давлением 22,5 кгс/см^2','температурой 180 °С и давлением 27,3 кгс/см^2'], #69
              'Какие клапаны установлены на двух "холодных" паропроводах, по которым пар подается в промежуточный пароперегреватель из ЦВД турбины?\nВыберите 1 правильный ответ:':['предохранительные','стопорные','обратные','шиберные задвижки'], #70
              'Что входит в состав КПП 1 ступени?\nВыберите 1 неправильный ответ:':['24 U-образны змеевика 32х6','входной коллектор 426х20','пакет змеевиков (342 шт. 50х4)','два выходных коллектора'], #71
              'Где установлен аварийный впрыскивающий пароохладитель?\nВыберите 1 правильный ответ:':['в каждом паропроводе между 1 и 2 ступенями КПП','во входном коллекторе КПП 1 ст.','в выходном коллекторе КПП 1 ст.','во входных коллекторах КПП 1 и 2 ст.'], #72
              'Куда поступает пар по паропроводу после выходного коллектора перегревателя 2 ст.?\nВыберите 1 правильный ответ:':['к отсечным клапанам ЦСД','в ЦВД','в ПНД','в ПВД'], #73
              'Как расположены пакеты КПП в/д и КПП 2 ст. вторично перегретого пара?\nВыберите 1 правильный ответ:':['на подвесных трубах','на каркасных балках','на фронтовом и боковом экранах НРЧ','на задней стенке конвективной шахты'], #74
              'Где расположены входные и выходные коллекторы подвесных труб?\nВыберите 1 правильный ответ:':['входной коллектор - в газоходе, выходной - на потолке поворотной камеры','входной коллектор - в топке, выходной – в газоходе','входной коллектор - в конвективной шахте, выходной – на фронтовой части топки','входной коллектор - на потолке поворотной камеры, выходной - на боковой части топки'], #75
              'Чем сопровождается действие защиты?\nВыберите 1 правильный ответ:':['светозвуковым сигналом',' текстовым оповещением','звуковым сигналом','световым сигналом'], #76
              'Укажите 1 неверное утверждение:':['действие защиты сопровождается только световым сигналом','обеспечивается определение первопричины срабатывания защиты','система защит предназначена для предотвращения возникновения и\n развития аварий при нарушениях нормального режима работы котла', 'в зависисмости от характера нарушения работы котлоагрегата защиты выполняют останов котла,\n снижение нагрузки котла, локальные операции'], #77
              'Как вводится в действие оборудование, отключенное защитой?\nВыберите 1 правильный ответ:':['дежурным персоналом КТЦ после устранения нарушения, вызвавшего срабатывание защиты','оборудование, отключенное защитой, не вводится в эксплуатацию','дежурным персоналом после вывода из эксплуатации резервного оборудования','дежурным персоналом ЦТАИ после вывода из эксплуатации резервного оборудования'], #78
              'Какие операции выполняют защиты котлоагрегата в зависимости от характера нарушения?\nВыберите 1 неправильный ответ:':['пуск котла','снижение нагрузки котла','локальные операции','останов котла'], #79
              'При каком значении давления природного газа после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:':['0,07 кгс/см^2','6,0 кгс/см^2','2,0 кгс/см^2','1,05 кгс/см^2'], #80
              'При каком значении давления мазута после регулирующих клапанов осуществляется аварийный останов котла защитой?\nВыберите 1 правильный ответ:':['4,0 кгс/см^2','60 кгс/см^2','2,0 кгс/см^2','1,05 кгс/см^2'], #81
              'Какое значение выдержки времени срабатывания защиты по понижению давления мазута после регулирующих клапанов предусмотрено при работе котла на мазуте?\nВыберите 1 правильный ответ:':['20 с','15 с','10 с','5 с'], #82
              'При достижении какого значения расхода питательной воды в котел срабатывает защита, осуществляющая аварийный останов котла?\nВыберите 1 правильный ответ:':['до 100 т/ч на нитку','до 200 т/ч на нитку','до 180т/ч на нитку','до 320 т/ч на нитку'], #83
              'С какой выдержкой по времени действует защита по прекращению поступления питательной воды в котел?\nВыберите 1 правильный ответ:':['30 с','50 с','90 с','9 с'], #84
              'При каком значении давления природного газа перед горелками срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:':['1,0 кгс/см^2','2,0 кгс/см^2','9,0 кгс/см^2','4,0 кгс/см^2'], #85
              'При каком минимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ':['200 кгс/см^2','180 кгс/см^2','100 кгс/см^2','220 кгс/см^2'], #86
              'С какой выдержкой по времени действует защита по понижению давления среды перед встроенной задвижкой?\nВыберите 1 правильный ответ:':['180 с','200 с','10 с','90 с'], #87
              'При каком максимальном значении давления среды перед встроенной задвижкой срабатывает защита на аварийный останов котла?\nВыберите 1 правильный ответ:':['320 кгс/см^2','100 кгс/см^2','400 кгс/см^2','300 кгс/см^2'], #88
              'При понижении давления среды перед встроенной задвижкой во время пуска до какого значения предусмотрен аварийный останов котла защитами?\nВыберите 1 правильный ответ:':['200 кг/см^2','400 кг/см^2','180 кг/см^2','350 кг/см^2'], #89
              'При каких значениях расхода пара через промежуточный пароперегреватель предусмотрен аварийный останов защитой?\nВыберите 1 правильный ответ:':['0,05 кгс/см^2','0,1 кгс/см^2','4,0 кгс/см^2','2,0 кгс/см^2'], #90
              'С какой выдержкой по времени действует защита по понижению расхода пара через промежуточный пароперегреватель?\nВыберите 1 правильный ответ:':['20 с','30 с','10 с','5 с'], #91
              'Как измеряется расход пара через промежуточный пароперегреватель?\nВыберите 1 правильный ответ:':['по перепаду давлений на всем пароперегревателе','ультразвуковыми расходомерами','вихревыми расходомерами','оптическими расходомерами'], #92
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дымососов?\nВыберите 2 правильных ответа:':['отключение электродвигателей обоих дымососов','отключение одного из дымососов, если другой не работает','отключение одного из дымососов','снижение нагрузки электродвигателей обоих дымососов'], #93
              'Когда предусмотрен аварийный останов защитами по отключению электродвигателей дутьевых вентиляторов?\nВыберите 2 правильных ответа:':['отключение электродвигателей обоих дутьевых вентиляторов','отключение одного из дутьевых вентиляторов, если другой не работает','отключение одного из дутьевых вентиляторов','снижение нагрузки электродвигателей обоих дутьевых вентиляторов'], #94
              'Когда предусмотрен аварийный останов защитами по останову РВП?\nВыберите 2 правильных ответа':['останов обоих РВП','останов одного РВП, если другой не работает','останов одного РВП','снижение нагрузки РВП'], #95
              'С какой выдержкой по времени предусмотрен аварийный останов при отключении обоих РВП?\nВыберите 1 правильный ответ:':['9 с','10 с','15 с','5 с'], #96
              'При каких условиях защита по понижению давления природного газа и мазута воздействует на останов котла?\nВыберите 1 неправильный ответ:':['если защиты по понижению давления природного газа и мазута действуют одновременно,\n то производится останов котла при положении выключателя "Газ",\n так как природный газ – основное топливо','по понижению давления природного газа воздействует \nтолько в положении переключателя топлива (ПТ) "Газ"','по понижению давления мазута - в положение "Мазут"','если защиты по понижению давления природного газа и мазута действуют одновременно,\n то производится останов котла независимо от положений переключателя топлива'], #97
              'В каких случаях предусматривается аварийный останов котла защитами?\nВыберите 2 неправильных ответа:':['повышение давления среды перед встроенной задвижкой во время пуска сверх установленного предела','повышение расхода пара через промежуточный пароперегреватель','повышение давления природного газа перед горелками','понижение давления среды перед встроенной задвижкой во время пуска до установленного предела'], #98
              'Какие операции выполняются одновременно при останове котла защитой одновременно выполняются следующие операции?\nВыберите 2 неправильных ответа:':['открытие быстрозапорного клапана на подводе мазута к котлу,\n с наложением запрета на закрытие задвижки','закрытие задвижек и шаровых кранов на продувочных свечах,\n а также задвижек на свечах безопасности газопровода при работе котла на газе и \nпри совместном сжигании газа и мазута','закрытие запорной задвижки и быстрозапорного клапана на подводе мазута к котлу,\n а также закрытие задвижки, закрытие всех задвижек на подводе мазута к форсункам','закрывается арматура на питательной воде (РПК) и на впрысках'], #99
              'Какие защиты, действующие на частичное снижение нагрузки блока, выполняются при наличии импульсной команды об отключении одного из механизмов?\nВыберите 1 неправильный ответ:':['отключении ПТН и включении ПЭН системой АВР','отключение электродвигателя одного из дутьевых вентиляторов\n при другом работающем','отключение электродвигателя одного из дымососов\n при другом работающем','останов одного из РВП при другом вращающемся'], #100
              'С какой выдержкой времени выполняются команды об отключении одного из механизмов при действии защит по частичному снижению нагрузки блока?\nВыберите 1 правильный ответ:':['2 с','10 с','8 с','15 с'], #101
              'В каких случаях выполняются защиты по отключению одного из механизмов, предусматривающие частичное снижение нагрузки блока?\nВыберите 2 правильных ответа:':['при наличии импульсной команды об отключении одного из механизмов с выдержкой времени','если не работала защита на останов блока','если не работает один из механизмов','при наличии выдержки времени отключения одного из механизмов более 5 с'], #102
              'С какой выдержкой времени действует защита по отключению ПТН и включению ПЭН системой АВР?\nВыберите 1 правильный ответ:':['до 9 с','до 2 с','до 15 с','до 20 с'], #103
              'При повышении температуры первичного пара перед турбиной до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:':['570 °С','450 °С','380 °С','650 °С'], #104
              'С какой выдержкой времени действует защита, предусматривающая частичное снижение нагрузки блока, при повышении температуры первичного пара перед турбиной?\nВыберите 1 правильный ответ:':['до 180 с','до 100 с','до 10 с','до 2 с'], #105
              'При повышении температуры вторичного пара на выходе из котла до каких значений действует защита, предусматривающая частичное снижение нагрузки блока?\nВыберите 1 правильный ответ:':['570 °С','450 °С','380 °С','650 °С'], #106
              'С какой выдержкой времени действует защита, предусматривающая частичное снижение нагрузки котла, при повышении температуры вторичного пара на выходе из котла?\nВыберите 1 правильный ответ:':['до 180 с','до 100 с','до 10 с','до 2 с'], #107
              'Какая нагрузка задается котлу системой автоматического регулирования при срабатывании любой защиты, предусматривающей снижение нагрузки котла?\nВыберите 1 правильный ответ:':['50-60 % номинальной','70-80 % номинальной','50-80 % номинальной','70-90 % номинальной'], #108
              'В каких случаях производится частичное снижение нагрузки блока?\nВыберите 2 неправильных ответа:':['при откючении ПЭН','при понижении расхода пара через промежуточный пароперегреватель\n до 50-60 % номинального','при повышении температуры первичного пара перед турбиной до 570 °С\n с подачей предупредительного сигнала на БЩУ','при отключении электродвигателя одного из дымососов\n при другом работающем'], #109
              'В каких случаях разрешается разгружение блока до 60% при срабатывании защит, действующих на снижение нагрузки блока?\nВыберите 1 правильный ответ:':['нагрузка блока была больше этого значения','котел работает на природном газе','котел работает на мазуте','используется замыкание блок-контактов приводов выключателей\n соответствующих электродвигателей'], #110
              'Как осуществляется контроль нагрузки при срабатывании защит, действующих на снижение нагрузки блока?\nВыберите 1 правильный ответ:':['по давлению в камере регулирующей ступени турбины','давления среды перед встроенной задвижкой','по давлению пара на выходе из котла','расхода пара через промежуточный пароперегреватель'], #111
              'Какие операций необходимо произвести при снижении нагрузки?\nВыберите 2 правильных ответа:':['включение регулятора давления на турбине "до себя"','отключение воздействия регулятора мощности блока на работающий регулятор топлива\n и к последнему подключается задатчик 50-60 % нагрузки','отключение электродвигателя одного \nиз дутьевых вентиляторов и дымососов','отключение воздействия регуляторов общего воздуха и разрежения\n на направляющие аппараты дутьевых вентиляторов'], #112
              'Как вводятся и выводятся защиты, действующие на снижение нагрузки блока?\nВыберите 1 правильный ответ:':['при отключении одного из двух работающих ДВ, ДС или РВП выводятся автоматически \nпри нагрузке ниже 60 %, вводятся автоматически при включении в работу обоих одноименных механизмов','при отключении одного из двух работающих ДВ, ДС или РВП выводятся автоматически\n при нагрузке ниже 50 %, вводятся дежурным персоналом ЦТАИ при включении в работу обоих одноименных механизмов','при отключении одного из двух работающих ДВ, ДС или РВП выводятся автоматически\n при нагрузке ниже 60 %, вводятся дежурным персоналом КТЦ при включении в работу\n обоих одноименных механизмов','при отключении одного из двух работающих ДВ, ДС или РВП выводятся дежурным персоналом КТЦ при нагрузке ниже 50 %,\n вводятся дежурным персоналом ЦТАИ при включении в работу обоих одноименных механизмов'], #113
              'При повышении давления острого пара в паропроводе перед ПСУ до первого предела, равного 1,05 РНОМ:\nВыберите 1 правильный ответ:':['открывается клапан ПСУ','принудительно открывается импульсный предохранительный клапан','открывается быстрозапорный клапан','открывается ПЗК'], #114
              'При повышении давления острого пара за котлом в любом паропроводе до 2 предела равного 1,1 номинального:\nВыберите 1 правильный ответ:':['подается сигнал на принудительное открытие импульсных предохранительных клапанов','подается сигнал на принудительное открытие клапана ПСУ','подается сигнал на принудительное закрытие импульсных предохранительных клапанов','подается сигнал на принудительное закрытие ПСУ'], #115
              'При каких условиях предусмотрена защита при повышении давления острого пара за котлом?\nВыберите 2 правильных ответа:':['при повышении давления острого пара в паропроводе перед ПСУ до первого предела, равного 1,05 РНОМ','при повышении давления острого пара за котлом в любом паропроводе до 2 предела равного 1,1 номинального','при повышении давления острого пара в паропроводе перед ПСУ до первого предела, равного 1,15 РНОМ','при повышении давления острого пара за котлом в любом паропроводе до 2 предела равного 1,25 номинального'], #116
              'Какие действия предусмотрены защитой при загорании отложений в РВП?\nВыберите 1 неправильный ответ:':['отключение воздействия регуляторов общего воздуха и разрежения\n на направляющие аппараты дутьевых вентиляторов и дымососов','включение средств пожаротушения','закрытие клапанов на газоходах и воздуховодах до и после','отключение соответствующего ДС и ДВ'], #117
              'Как производится включение средств пожаротушения при загорании отложений в РВП?\nВыберите 1 правильный ответ:':['по уменьшению разности температуры горячего воздуха после РВП и уходящих газов\n до РВП до минус 20 °С открываются задвижки на подводе воды к соответствующему РВП','по уменьшению разности температуры горячего воздуха после РВП и уходящих газов\n до РВП до 5 °С открываются задвижки на подводе воды к соответствующему РВП','по уменьшению разности температуры горячего воздуха после РВП и уходящих газов\n до РВП до минус 10 °С закрываются задвижки на подводе воды к соответствующему РВП','по уменьшению разности температуры горячего воздуха после РВП и уходящих газов\n до РВП до 10 °С закрываются задвижки на подводе воды к соответствующему РВП'], #118
              'Какое значение является предельным при повышении температуры вторичного пара за котлом?\nВыберите 1 правильный ответ:':['570 °С','450 °С','610 °С','520 °С'], #119
              'Какие операции производятся при срабатывании защиты при повышении температуры вторичного пара выше предельного уровня?\nВыберите 1 правильный ответ:':['при начале открытия какого-либо из клапанов аварийного впрыска открывается вентиль\n на трубопроводе питательной воды к аварийным впрыскам во вторичный пароперегреватель','при начале открытия всех клапанов аварийного впрыска открывается вентиль\n на трубопроводе питательной воды к аварийным впрыскам во вторичный пароперегреватель','при начале закрытия всех клапанов аварийного впрыска  открывается вентиль на трубопроводе питательной воды\n к аварийным впрыскам во вторичный пароперегреватель','при начале открытия одного из клапанов аварийного впрыска закрывается вентиль\n на трубопроводе питательной воды к аварийным впрыскам во вторичный пароперегреватель'], #120
              'На каких горелках смонтирована и налажена защита по не воспламенению или погасанию факела?\nВыберите 2 правильных ответа:':['на всех','на любой растопочной','только на горелках № 1, 2, 3, 4','только на горелках № 5, 6, 7, 8'], #121
              'Как производится контроль наличия факела горелки во время розжига?\nВыберите 1 правильный вариант:':['после начала открытия задвижки (схода с установки концевого выключателя\n на закрытое положение задвижки) на центральном подводе газа к горелкам','после повышения давления топлива на 10% от номинального,\n на центральном подводе газа к горелкам','после повышения температуры в топке до номинального значения,\n на центральном подводе газа к горелкам','после установления устойчивого режима горения топлива,\n на центральном подводе газа к горелкам'], #122
              'Через какой промежуток времени срабатывает защита на отключение горелки при не воспламенении или погасании факела включаемой в работу растопочной горелки в процессе розжига?\nВыберите 1 правильный ответ:':['9 с','5 с','15 с','10 с'], #123
              'При повышении давления газа за регулирующим клапаном выше какого значения уставки срабатывает защита по понижению давления газа?\nВыберите 1 правильный ответ:':['Рг > 0,07 кг/см^2','Рг > 1кг/см^2','Рг > 1,05 кг/см^2','Рг > 0,05 кг/см^2'], #124
              'Какими средствами измерения контролируется давлении газа за регулирующим клапаном?\nВыберите 1 правильный ответ:':['электроконтактными манометрами','пьезоэлектрическими манометрами','ионизационными манометрами','тепловые манометры'], #125
              'Когда выводится защита по понижению давления газа за   регулирующим клапаном?\nВыберите 2 правильных ответа:':['при вводе защиты по погасанию общего факела в топке','от концевого выключателя при закрытой задвижке на подводе газа к котлу','при вводе защиты по не воспламенению или погасанию факела любой растопочной горелки','от концевого выключателя при закрытой задвижке на подводе воздуха к котлу'], #126
              'Когда разрешается розжиг горелок, не используемых при растопке котла?\nВыберите 1 правильный ответ:':['после розжига всех горелок растопочной группы','во время растопки котла','при не воспламенении или погасании факела на горелках, входящих в растопочную группу','при работе котла на 50% нагрузке'], #127
              'Когда снимается блокировка на запрет открытия задвижек и включение ЗЗУ на горелки, не входящих в растопочную группу?\nВыберите 1 правильный ответ:':['после ввода защиты по погасанию общего факела в топке переводом ключа\n управления 2ПЗ в положение "Включено"','после вывода защиты по погасанию общего факела в топке переводом ключа управления 2ПЗ в положение "Выключено"','после ввода защиты по погасанию факела одной из растопочных горелок автоматически','после ввода защиты по погасанию общего факела в топке автоматически'], #128
              'Кто производит опробование защит на "сигнал", в соответствии с графиком опробования защит энергоблоков?\nВыберите 1 правильный ответ:':['оперативный персонал КТО совместно с оперативным персоналом ЦТАИ','оперативный персонал КТО','оперативный персонал электрического цеха','оперативный персонал КТО совместно с оперативным персоналом электрического цеха'], #129
            }

#список правильных ответов
correct_answer = ['Т-250/300-240;', 'Т-250/300-240.', #1
                  'по растопочным расходомерам;','датчиками на пониженный перепад давления;', 'по растопочным расходомерам.','датчиками на пониженный перепад давления.', #2
                  'пар сверхкритического давления с температурой перегрева 545°С;', 'пар сверхкритического давления с температурой перегрева 545°С.', #3
                  'природного газа и мазута;', 'природного газа и мазута.', #4
                  'ТГМП-314П - котельный агрегат прямоточный, с П-образной однокорпусной компоновкой;', 'ТГМП-314П - котельный агрегат прямоточный, с П-образной однокорпусной компоновкой.', #5
                  '2 регенеративных воздухоподогревателя;', '2 регенеративных воздухоподогревателя.', #6
                  'газо-импульсная термоволновая очистка;','газо-импульсная термоволновая очистка.', #7
                  'два дутьевых вентилятора ВД-2,8 одностороннего всасывания;', 'два дымососа рециркуляции дымовых газов одностороннего всасывания типа ДРГ-25;','два дутьевых вентилятора ВД-2,8 одностороннего всасывания.', 'два дымососа рециркуляции дымовых газов одностороннего всасывания типа ДРГ-25.', #8
                  'в качестве горелочных устройств использованы газо-мазутные горелки,\n расположенные вертикально в два ряда в поду топочной камеры;','в качестве горелочных устройств использованы газо-мазутные горелки,\n расположенные вертикально в два ряда в поду топочной камеры.', #9
                  'на периферийном и центральнном каналах установлены завихрители;','на периферийном и центральнном каналах установлены завихрители.', #10
                  'в диапазоне от минус 30°С (с использованием рециркуляции подогретого воздуха)\n до плюс 45°С;','в диапазоне от минус 30°С (с использованием рециркуляции подогретого воздуха)\n до плюс 45°С.', #11
                  '8,9 т/ч;','8,9 т/ч.', #12
                  '10,5*10^3 нм^3/ч;','10,5*10^3 нм^3/ч.', #13
                  'паромеханические форсунки типа "Эдипол";','паромеханические форсунки типа "Эдипол".', #14
                  'турбонасосом;', 'пускорезервным электронасосом;','турбонасосом.', 'пускорезервным электронасосом.', #15
                  'турбонасос - 1100 т/ч, электронасос - 600 т/ч;','турбонасос - 1100 т/ч, электронасос - 600 т/ч.', #16
                  'два несмешиваемых потока;','два несмешиваемых потока.', #17
                  'питательным насосом;','питательным насосом.', #18
                  'распределение питательной воды по потокам;','распределение питательной воды по потокам.', #19
                  'одинаковыми;','одинаковыми.', #20
                  'экраны поворотной камеры;', 'ширмы;','экраны поворотной камеры.', 'ширмы.', #21
                  'приведенная последовательность включения поверхностей нагрева по ходу среды\n в пароводяном тракте котла является правильной;','приведенная последовательность включения поверхностей нагрева по ходу среды\n в пароводяном тракте котла является правильной.', #22
                  'на трубопроводе между ПЭ и ШПП;','на трубопроводе между ПЭ и ШПП.', #23
                  'встроенными сепараторами с соответствующей дроссельной арматурой;','встроенными сепараторами с соответствующей дроссельной арматурой.', #24
                  'по ходу пара в каждом потоке последовательно установлено\n две ступени пароперегревателя;','по ходу пара в каждом потоке последовательно установлено\n две ступени пароперегревателя.', #25
                  'от 30 до 100%;','от 30 до 100%.', #26
                  'от 50 до 100%;','от 50 до 100%.', #27
                  '"топливо-вода";','"топливо-вода".', #28
                  'с помощью двух впрысков;','с помощью двух впрысков.', #29
                  'первый впрыск - перед ширмовым пароперегревателем,\n второй - перед конвективным пароперегревателем;','первый впрыск - перед ширмовым пароперегревателем,\n второй - перед конвективным пароперегревателем.', #30
                  'рециркуляция дымовых газов;', 'аварийный впрыск;','рециркуляция дымовых газов.', 'аварийный впрыск.', #31
                  'перед 2-й ступенью пароперегревателя;','перед 2-й ступенью пароперегревателя.', #32
                  'за ВЭ;','за ВЭ.', #33
                  'пусковыми впрысками в паропроводы;','паровыми байпасами промперегревателя;','пусковыми впрысками в паропроводы.','паровыми байпасами промперегревателя.', #34
                  'вода на впрыск в пароохладители свежего пара подается из питательного трубопровода,\n а в паропроводы вторично перегретого пара из промступеней питательных насосов;','вода на впрыск в пароохладители свежего пара подается из питательного трубопровода,\n а в паропроводы вторично перегретого пара из промступеней питательных насосов.', #35
                  'одним трубопроводом  377х45 ст. 15 ГС;','одним трубопроводом  377х45 ст. 15 ГС.', #36
                  'обратный клапан;','обратный клапан.', #37
                  'на впрыски в паровой тракт котла;','на впрыски в паровой тракт котла.', #38
                  'за обратным клапаном питательный трубопровод разделяется на две нитки "А" и "Б",\n каждая из которых становится самостоятельно регулируемым потоком;','за обратным клапаном питательный трубопровод разделяется на две нитки "А" и "Б",\n каждая из которых становится самостоятельно регулируемым потоком.', #39
                  'во входной коллектор водяного экономайзера;','во входной коллектор водяного экономайзера.', #40
                  '273х40;','273х40.', #41
                  '123;','123.', #42
                  '2;','2.', #43
                  'во входной коллектор подвесных труб;','во входной коллектор подвесных труб.', #44
                  '159;','159.', #45
                  'тремя лентами (по 53 трубы);','тремя лентами (по 53 трубы).', #46
                  'после выходных коллекторов 219х36, расположенных на потолке конвективной шахты;','после выходных коллекторов 219х36, расположенных на потолке конвективной шахты.', #47
                  'без разделительных коллекторов, деление поверхности нагрева на СРЧ и ВРЧ условное;','без разделительных коллекторов, деление поверхности нагрева на СРЧ и ВРЧ условное.', #48
                  'из 9 панелей, каждая из которых образована 23 змеевиками из труб 32х6;','из 9 панелей, каждая из которых образована 23 змеевиками из труб 32х6.', #49
                  'в 9 выходных коллекторов 159х28;','в 9 выходных коллекторов 159х28.', #50
                  'на фронтовой стене топки в верхней её части;','на фронтовой стене топки в верхней её части.', #51
                  'в 3 выходные камеры экрана поворотной камеры, а затем в 3 входные камеры потолочного экрана;','в 3 выходные камеры экрана поворотной камеры, а затем в 3 входные камеры потолочного экрана.', #52
                  '180 змеевиков 38х6;','180 змеевиков 38х6.', #53
                  'врезана в смесительный коллектор 325х45, расположенный в конвективной шахте;','врезана в смесительный коллектор 325х45, расположенный в конвективной шахте.', #54
                  'перед ВЗ;','перед ВЗ.', #55
                  'в виде вертикальной трубы 377х60;','в виде вертикальной трубы 377х60.', #56
                  'в верхнее донышко, осевой подвод;','в верхнее донышко, осевой подвод.', #57
                  'вода отбрасывается к наружным стенкам и через горизонтальный\n штуцер направляется в растопочный расширитель;', 'пар - через диффузор в нижнем донышке по трубопроводу - в коллектор,\n на котором установлен пароохладитель (впрыск 1), а из него подводится к ШПП 1 ст.;','вода отбрасывается к наружным стенкам и через горизонтальный\n штуцер направляется в растопочный расширитель.','пар - через диффузор в нижнем донышке по трубопроводу - в коллектор,\n на котором установлен пароохладитель (впрыск 1), а из него подводится к ШПП 1 ст..', #58
                  'после конического рассекателя;', 'после лопаток завихрителя;','после конического рассекателя.', 'после лопаток завихрителя.', #59
                  'на коллекторе за встроенной задвижкой перед ШПП 1 ст.;','на коллекторе за встроенной задвижкой перед ШПП 1 ст..', #60
                  'входным и выходным коллектором 155х28;', '24-я U-образными змеевиками 32х6;','входным и выходным коллектором 155х28.', '24-я U-образными змеевиками 32х6.', #61
                  'на выходном коллекторе ШПП 2 ст.;','на выходном коллекторе ШПП 2 ст..', #62
                  'в конвективный пароперегреватель;','в конвективный пароперегреватель.', #63
                  'прямоточная;','прямоточная.', #64
                  'с температурой 545 °С и давлением 255 кг/см^2;','с температурой 545 °С и давлением 255 кг/см^2.', #65
                  'за котлом на главном трубопроводе;','за котлом на главном трубопроводе.', #66
                  'четыре главных предохранительных клапана Ду-125;', 'четыре импульсных клапана Ду-20;','четыре главных предохранительных клапана Ду-125.', 'четыре импульсных клапана Ду-20.', #67
                  'перед стопорными клапанами турбины;','перед стопорными клапанами турбины.', #68
                  'температурой 297 °С и давлением 40,3 кгс/см^2;','температурой 297 °С и давлением 40,3 кгс/см^2.', #69
                  'предохранительные;','предохранительные.', #70
                  'входной коллектор 426х20;','входной коллектор 426х20.', #71
                  'в каждом паропроводе между 1 и 2 ступенями КПП;','в каждом паропроводе между 1 и 2 ступенями КПП.', #72
                  'к отсечным клапанам ЦСД;','к отсечным клапанам ЦСД.', #73
                  'на подвесных трубах;','на подвесных трубах.', #74
                  'входной коллектор - в газоходе, выходной - на потолке поворотной камеры;','входной коллектор - в газоходе, выходной - на потолке поворотной камеры.', #75
                  'светозвуковым сигналом;','светозвуковым сигналом.', #76
                  'действие защиты сопровождается только световым сигналом;','действие защиты сопровождается только световым сигналом.', #77
                  'дежурным персоналом КТЦ после устранения нарушения, вызвавшего срабатывание защиты;','дежурным персоналом КТЦ после устранения нарушения, вызвавшего срабатывание защиты.', #78
                  'пуск котла;','пуск котла.', #79
                  '0,07 кгс/см^2;','0,07 кгс/см^2.', #80
                  '4,0 кгс/см^2;','4,0 кгс/см^2.', #81
                  '20 с;','20 с.', #82
                  'до 100 т/ч на нитку;','до 100 т/ч на нитку.', #83
                  '30 с;','30 с.', #84
                  '1,0 кгс/см^2;','1,0 кгс/см^2.', #85
                  '200 кгс/см^2;','200 кгс/см^2.', #86
                  '180 с;','180 с.', #87
                  '320 кгс/см^2;','320 кгс/см^2.', #88
                  '200 кг/см^2;','200 кг/см^2.', #89
                  '0,05 кгс/см^2;','0,05 кгс/см^2.', #90
                  '20 с;','20 с.', #91
                  'по перепаду давлений на всем пароперегревателе;','по перепаду давлений на всем пароперегревателе.', #92
                  'отключение электродвигателей обоих дымососов;', 'отключение одного из дымососов, если другой не работает;','отключение электродвигателей обоих дымососов.', 'отключение одного из дымососов, если другой не работает.', #93
                  'отключение электродвигателей обоих дутьевых вентиляторов;', 'отключение одного из дутьевых вентиляторов, если другой не работает;','отключение электродвигателей обоих дутьевых вентиляторов.', 'отключение одного из дутьевых вентиляторов, если другой не работает.', #94
                  'останов обоих РВП;', 'останов одного РВП, если другой не работает;','останов обоих РВП.', 'останов одного РВП, если другой не работает.', #95
                  '9 с;','9 с.', #96
                  'если защиты по понижению давления природного газа и мазута действуют одновременно,\n то производится останов котла при положении выключателя "Газ",\n так как природный газ – основное топливо;','если защиты по понижению давления природного газа и мазута действуют одновременно,\n то производится останов котла при положении выключателя "Газ",\n так как природный газ – основное топливо.', #97
                  'повышение давления среды перед встроенной задвижкой во время пуска сверх установленного предела;', 'повышение расхода пара через промежуточный пароперегреватель;','повышение давления среды перед встроенной задвижкой во время пуска сверх установленного предела.', 'повышение расхода пара через промежуточный пароперегреватель.', #98
                  'открытие быстрозапорного клапана на подводе мазута к котлу,\n с наложением запрета на закрытие задвижки;', 'закрытие задвижек и шаровых кранов на продувочных свечах,\n а также задвижек на свечах безопасности газопровода при работе котла на газе и \nпри совместном сжигании газа и мазута;','открытие быстрозапорного клапана на подводе мазута к котлу,\n с наложением запрета на закрытие задвижки.', 'закрытие задвижек и шаровых кранов на продувочных свечах,\n а также задвижек на свечах безопасности газопровода при работе котла на газе и \nпри совместном сжигании газа и мазута.', #99
                  'отключении ПТН и включении ПЭН системой АВР;','отключении ПТН и включении ПЭН системой АВР.', #100
                  '2 с;','2 с.', #101
                  'при наличии импульсной команды об отключении одного из механизмов с выдержкой времени;', 'если не работала защита на останов блока;','при наличии импульсной команды об отключении одного из механизмов с выдержкой времени.', 'если не работала защита на останов блока.', #102
                  'до 9 с;','до 9 с.', #103
                  '570 °С;','570 °С.', #104
                  'до 180 с;','до 180 с.', #105
                  '570 °С;','570 °С.', #106
                  'до 180 с;','до 180 с.', #107
                  '50-60 % номинальной;','50-60 % номинальной.', #108
                  'при откючении ПЭН;','при понижении расхода пара через промежуточный пароперегреватель\n до 50-60 % номинального;','при откючении ПЭН.','при понижении расхода пара через промежуточный пароперегреватель\n до 50-60 % номинального.', #109
                  'нагрузка блока была больше этого значения;','нагрузка блока была больше этого значения.', #110
                  'по давлению в камере регулирующей ступени турбины;','по давлению в камере регулирующей ступени турбины.', #111
                  'включение регулятора давления на турбине "до себя";','отключение воздействия регулятора мощности блока на работающий регулятор топлива\n и к последнему подключается задатчик 50-60 % нагрузки;','включение регулятора давления на турбине "до себя".','отключение воздействия регулятора мощности блока на работающий регулятор топлива\n и к последнему подключается задатчик 50-60 % нагрузки.', #112
                  'при отключении одного из двух работающих ДВ, ДС или РВП выводятся автоматически \nпри нагрузке ниже 60 %, вводятся автоматически при включении в работу обоих одноименных механизмов;','при отключении одного из двух работающих ДВ, ДС или РВП выводятся автоматически \nпри нагрузке ниже 60 %, вводятся автоматически при включении в работу обоих одноименных механизмов.', #113
                  'открывается клапан ПСУ;','открывается клапан ПСУ.', #114
                  'подается сигнал на принудительное открытие импульсных предохранительных клапанов;','подается сигнал на принудительное открытие импульсных предохранительных клапанов.', #115
                  'при повышении давления острого пара в паропроводе перед ПСУ до первого предела, равного 1,05 РНОМ;', 'при повышении давления острого пара за котлом в любом паропроводе до 2 предела равного 1,1 номинального;','при повышении давления острого пара в паропроводе перед ПСУ до первого предела, равного 1,05 РНОМ.', 'при повышении давления острого пара за котлом в любом паропроводе до 2 предела равного 1,1 номинального.', #116
                  'отключение воздействия регуляторов общего воздуха и разрежения\n на направляющие аппараты дутьевых вентиляторов и дымососов;','отключение воздействия регуляторов общего воздуха и разрежения\n на направляющие аппараты дутьевых вентиляторов и дымососов.', #117
                  'по уменьшению разности температуры горячего воздуха после РВП и уходящих газов\n до РВП до минус 20 °С открываются задвижки на подводе воды к соответствующему РВП;','по уменьшению разности температуры горячего воздуха после РВП и уходящих газов\n до РВП до минус 20 °С открываются задвижки на подводе воды к соответствующему РВП.', #118
                  '570 °С;','570 °С.', #119
                  'при начале открытия какого-либо из клапанов аварийного впрыска открывается вентиль\n на трубопроводе питательной воды к аварийным впрыскам во вторичный пароперегреватель;','при начале открытия какого-либо из клапанов аварийного впрыска открывается вентиль\n на трубопроводе питательной воды к аварийным впрыскам во вторичный пароперегреватель.', #120
                  'на всех;', 'на любой растопочной;','на всех.', 'на любой растопочной.', #121
                  'после начала открытия задвижки (схода с установки концевого выключателя\n на закрытое положение задвижки) на центральном подводе газа к горелкам;','после начала открытия задвижки (схода с установки концевого выключателя\n на закрытое положение задвижки) на центральном подводе газа к горелкам.', #122
                  '9 с;','9 с.', #123
                  'Рг > 0,07 кг/см^2;','Рг > 0,07 кг/см^2.', #124
                  'электроконтактными манометрами;', 'электроконтактными манометрами.',#125
                  'при вводе защиты по погасанию общего факела в топке;', 'от концевого выключателя при закрытой задвижке на подводе газа к котлу;','при вводе защиты по погасанию общего факела в топке.', 'от концевого выключателя при закрытой задвижке на подводе газа к котлу.', #126
                  'после розжига всех горелок растопочной группы;','после розжига всех горелок растопочной группы.', #127
                  'после ввода защиты по погасанию общего факела в топке переводом ключа\n управления 2ПЗ в положение "Включено";','после ввода защиты по погасанию общего факела в топке переводом ключа\n управления 2ПЗ в положение "Включено".', #128
                  'оперативный персонал КТО совместно с оперативным персоналом ЦТАИ;','оперативный персонал КТО совместно с оперативным персоналом ЦТАИ.', #129
                ]


if __name__ == '__main__':
     app = QtWidgets.QApplication(sys.argv)
     window = Start()
     window.show()
     sys.exit(app.exec_())









