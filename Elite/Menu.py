from Utils    import clear, requirements_module, create_directory, GeoLocator, GetUserCount
from Banner   import Logo1, Back, BelumTersedia, UserPanel, MainMenu, Choose, MenuDump, MenuSettings, License
from Login    import CheckLogin, Logout
from Color    import bold_putih, bold_merah, bold_lime, bold_cyan, bold_kuning
from Dump     import DumpEmail, DumpPhone, DumpFriend, DumpGroup, DumpName, DumpPost, DumpFollowers, DumpRandomID
from Crack    import Crack
from Settings import UserAgent, FileManager

class Main():

    def __init__(self):
        Logo1()
        UserAgent().DefaultSetup()
        self.MenuUserPanel()
        self.MenuMainMenu()

    def MenuUserPanel(self):
        self.user = CheckLogin()
        UserPanel(
            user_id      = GetUserCount().get('user_id'),
            user_name    = 'Test Launching',
            account_id   = self.user.id,#'100000721771295',
            account_name = self.user.name,#'Hanasta Rayartha Abinaya',
            status       = '{}Tester'.format(bold_kuning),
            ip           = GeoLocator())

    def MenuMainMenu(self):
        MainMenu()
        ch = Choose()
        match ch:
            case 0: Logout()
            case 1: self.menuDump(); Back()
            case 2: self.menuCrack()
            case 3: BelumTersedia(); Back()
            case 4: FileManager().ControlFileResult()
            case 5: License(); Back()
            case 6: self.menuSetting()
            case _: exit('{}Isi Yang Benar!{}'.format(bold_merah, bold_putih))

    def menuDump(self):
        MenuDump(self.user.isLogin)
        ch = Choose()
        print('')
        match ch:
            case 0: Back()
            case 1: BelumTersedia(); Back() # DumpEmail()
            case 2: BelumTersedia(); Back() # DumpPhone()
            case 3: DumpFriend(self.user.isLogin)
            case 4: DumpGroup(self.user.isLogin)
            case 5: DumpName(self.user.isLogin)
            case 6: DumpPost(self.user.isLogin)
            case 7: DumpFollowers(self.user.isLogin)
            case 8: DumpRandomID(self.user.isLogin)
            case _: exit('{}Isi Yang Benar!{}'.format(bold_merah, bold_putih))

    def menuCrack(self):
        print('')
        CR = Crack()
        CR.ChooseFile()
        CR.ChooseMethode()
        CR.AddCustomPassword()
        CR.SetUserAgent()
        CR.CreateFileResult()
        CR.Start()

    def menuSetting(self):
        MenuSettings()
        ch = Choose()
        match ch:
            case 0: Back()
            case 1: UserAgent().Menu()
            case 2: FileManager().Main()
            case _: exit('{}Isi Yang Benar!{}'.format(bold_merah, bold_putih))