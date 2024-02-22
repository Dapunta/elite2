import os, sys, time, requests, re, json, random, base64, uuid
from concurrent.futures import ThreadPoolExecutor
from Color import bold_putih, bold_cyan, bold_merah
from Utils import clear, HeadersGetWindows, HeadersPostWindows, HeadersGetAndroid, GetTime, ConvertURL, ConvertID, GetData, GetDataNoLogin, GetTokenEAAB, GetTokenEAAG

#--> Baca Cookie
def CurrentCookies():
    try:
        path = open('login/cookie.txt','r').read()
        return(path)
    except Exception as e:
        open('login/cookie.txt','a+')
        clear()
        exit('{}Jalankan Ulang Toolsnya!{}\n'.format(bold_merah, bold_putih))

#--> Pilihan Nama File
def SaveFile():
    filename = input('{}Tulis Nama File Baru : '.format(bold_putih))
    if filename == '' or filename == ' ': a, b, c, d, e, f = GetTime(); filename = '{}{}{}_{}{}{}'.format(a, b, c, d, e, f)
    savefile = 'dump/{}.txt'.format(filename)
    if os.path.exists(savefile):
        t = input('File Sudah Ada, [ganti/timpa/skip] [g/t/s] : ').lower()
        if t in ['g', 'ganti']: open(savefile, 'w').write('')
        elif t in ['t', 'timpa']: pass
        else: a, b, c, d, e, f = GetTime(); savefile = 'dump/{}{}{}_{}{}{}.txt'.format(a, b, c, d, e, f)
    open(savefile, 'a+'); print('')
    return(savefile)

#--> Input Target
def InputTarget1():
    print('{}Banyak Target, Pisahkan Dengan Koma (,)'.format(bold_putih))
    list_target = input('{}ID/URL Target : '.format(bold_putih)).split(',')
    return(list_target)
def InputTarget2():
    print('{}Banyak Nama, Pisahkan Dengan Koma (,)'.format(bold_putih))
    list_target = input('{}Nama Target : '.format(bold_putih)).split(',')
    return(list_target)

#--> Menampilkan Target
def PrintTarget1(target, id, name):
    print(target)
    print('{}ID   : {}{}'.format(bold_putih, str(id), bold_putih))
    print('{}Name : {}{}'.format(bold_putih, str(name), bold_putih))
def PrintTarget2(target, id, name, type, member):
    print(target)
    print('{}ID     : {}{}'.format(bold_putih, str(id), bold_putih))
    print('{}Name   : {}{}'.format(bold_putih, str(name), bold_putih))
    print('{}Type   : {}{}'.format(bold_putih, str(type), bold_putih))
    print('{}Member : {}{}'.format(bold_putih, str(member), bold_putih))

#--> Menyimpan Hasil Dump
def SaveResult(file, format):
    try:
        text = '{}\n'.format(str(format.encode('utf-8')).replace("b'",'').replace("'",'').replace('"','').replace('-',' ').replace('Jr.','').replace('jr.','').replace('_',' ').strip())
        if text.startswith('b'): text = text.lstrip('b')
        id = text.split('|')[0]
        if (len(str(id)) == 15) and (not str(id).startswith('1000')): tur = False
        else:
            if (text in open(file, 'r').read().splitlines()) or ('\\' in str(text)): tur = False
            else: open(file, 'a+').write(text); tur = True
    except Exception as e: tur = False
    return(tur)

#--> Menampilkan Lokasi File
def FinishFile(filename):
    opfile = open(filename,'r')
    print('{}Success Dump Total {}{} {}ID'.format(bold_putih, bold_cyan, str(len(opfile.read().splitlines())), bold_putih))
    print('{}File Saved At {}{}{}'.format(bold_putih, bold_cyan, str(filename), bold_putih))
    print('')
    opfile.close()

#--> Error Spam
def Spam():
    print('{}Maaf, Akunmu Terkena {}Spam{}.'.format(bold_putih, bold_merah, bold_putih))
    print('')

#--> Berhenti
def ctrlc():
    print('{}Tekan {}ctrl{}+{}c {}Untuk Berhenti'.format(bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih))
    print('')

#--> Harus Login
def HarusLogin():
    print('{}Anda Harus Login Untuk Menggunakan Fitur Ini!{}\n'.format(bold_merah, bold_putih))
    exit()

#--> Select Dump With Cookie Or Token
def DumpSelector():
    x = input('{}Dump Dengan Cookie/Token [{}c{}/{}t{}] : {}'.format(bold_putih, bold_cyan, bold_putih, bold_cyan, bold_putih, bold_cyan)).lower()
    return('token' if x in ['t', 'token', '2'] else 'cookie')

#--> Dump Friendlist
class DumpFriend():

    def __init__(self, isLogin):
        if not isLogin: HarusLogin()
        self.cookie = CurrentCookies()
        self.loop = 0

        cond = DumpSelector()
        if cond == 'token':
            try:
                token = GetTokenEAAB(self.cookie)
            except Exception as e:
                cond, token = 'cookie', 'null'
                print('{}Gagal Mengambil Token!'.format(bold_merah), end='', flush=True)
                time.sleep(2)
                print('\r{}'.format(bold_putih), end='')

        list_target = InputTarget1()
        self.save_file = SaveFile()
        ctrlc()
        for target in list_target:
            self.loop += 1; self.loopdump = 0
            r = requests.Session()
            url = ConvertURL(target)
            try: req = r.get(url, headers=HeadersGetWindows(), cookies={'cookie':self.cookie}, allow_redirects=True).text.replace('\\','')
            except Exception as e: req = 'null'
            info, id = self.ShowInfo(target, req)
            id = str(id).split('m')[-1]
            if req != 'null' and info == 1:
                if cond == 'token':
                    url = 'https://graph.facebook.com/v13.0/{}/friends'.format(id)
                    resp = r.get(url, params={'access_token':token}, cookies={'cookie':self.cookie}).json()
                    self.DumpToken(r, url, token, resp)
                else:
                    Data = GetData(req)
                    tab_key = re.search(r'{"tab_key":"friends_all","id":"(.*?)"}',str(req)).group(1)
                    self.DumpCookie(r, Data, tab_key, None)
            print('\rSuccess Dump {} ID'.format(str(self.loopdump)))
            print('')
            r.close()
        FinishFile(self.save_file)

    def ShowInfo(self, target, req):
        try:
            if target == 'me': a, b = list(re.findall(r'"USER_ID":"(.*?)","NAME":"(.*?)"',str(req))[0])
            else: a, b = list(re.findall(r'"ProfileActionBlock","profile_owner":{"id":"(.*?)","name":"(.*?)","gender"',str(req))[0])
            tg, id, name, tur = '{}[{}{}{}] {}{}'.format(bold_cyan, bold_putih, str(self.loop), bold_cyan, str(target), bold_putih), '{}{}'.format(bold_cyan, a), '{}{}'.format(bold_cyan, b), 1
        except Exception as e: tg, id, name, tur = '{}[{}{}{}] {}{}'.format(bold_merah, bold_putih, str(self.loop), bold_merah, str(target), bold_putih), '{}Not Found'.format(bold_merah), '{}Unknown'.format(bold_merah), 0
        PrintTarget1(tg, id, name)
        return(tur, id)

    def DumpCookie(self, r, Data, tab_key, cursor):
        try:
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','variables':json.dumps({"count":8,"cursor":cursor,"scale":2,"search":None,"id":tab_key}),'server_timestamps':True,'doc_id':'6709724792472394'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    rw = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']
                    id, nm, un = str(rw['id']), str(rw['name']), str(x['node']['url']).replace('https://www.facebook.com/','').replace('profile.php?id=','')
                    fm = '{}|{}|{}'.format(id, un, nm)
                    if str(un) != 'None':
                        if SaveResult(self.save_file, fm): self.loopdump += 1
                        print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            if pos['data']['node']['pageItems']['page_info']['has_next_page']:
                end_cursor = pos['data']['node']['pageItems']['page_info']['end_cursor']
                self.DumpCookie(r, Data, tab_key, end_cursor)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def DumpToken(self, r, url, token, resp):
        try:
            for i in resp['data']:
                try:
                    fm = '{}|{}|{}'.format(i['id'], i['id'], i['name'])
                    if SaveResult(self.save_file, fm): self.loopdump += 1
                    print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            after = resp['paging']['cursors']['after']
            new_resp = r.get(url, params={'access_token':token,'after':after,'pretty':'1'}, cookies={'cookie':self.cookie}).json()
            self.DumpToken(r, url, token, new_resp)
        except KeyboardInterrupt: pass
        except Exception as e: pass

#--> Dump Follower
class DumpFollowers():

    def __init__(self, isLogin):
        if not isLogin: HarusLogin()
        self.cookie = CurrentCookies()
        self.loop = 0

        cond = DumpSelector()
        if cond == 'token':
            try:
                token = GetTokenEAAG(self.cookie)
            except Exception as e:
                cond, token = 'cookie', 'null'
                print('{}Gagal Mengambil Token!'.format(bold_merah), end='', flush=True)
                time.sleep(2)
                print('\r{}'.format(bold_putih), end='')

        list_target = InputTarget1()
        self.save_file = SaveFile()
        ctrlc()
        for target in list_target:
            self.loop += 1; self.loopdump = 0
            r = requests.Session()
            url = ConvertURL(target)
            try: req = r.get(url, headers=HeadersGetWindows(), cookies={'cookie':self.cookie}, allow_redirects=True).text.replace('\\','')
            except Exception as e: req = 'null'
            info, id = self.ShowInfo(target, req)
            id = str(id).split('m')[-1]
            if req != 'null' and info == 1:
                if cond == 'token':
                    url = 'https://graph.facebook.com/v1.0/{}/subscribers'.format(id)
                    resp = r.get(url, params={'access_token':token}, cookies={'cookie':self.cookie}).json()
                    self.DumpToken(r, url, token, resp)
                else:
                    Data = GetData(req)
                    tab_key = re.search(r'{"tab_key":"followers","id":"(.*?)"}',str(req)).group(1)
                    self.DumpCookie(r, Data, tab_key, None)
            print('\rSuccess Dump {} ID'.format(str(self.loopdump)))
            print('')
            r.close()
        FinishFile(self.save_file)

    def ShowInfo(self, target, req):
        try:
            if target == 'me': a, b = list(re.findall(r'"USER_ID":"(.*?)","NAME":"(.*?)"',str(req))[0])
            else: a, b = list(re.findall(r'"ProfileActionBlock","profile_owner":{"id":"(.*?)","name":"(.*?)","gender"',str(req))[0])
            tg, id, name, tur = '{}[{}{}{}] {}{}'.format(bold_cyan, bold_putih, str(self.loop), bold_cyan, str(target), bold_putih), '{}{}'.format(bold_cyan, a), '{}{}'.format(bold_cyan, b), 1
        except Exception as e: tg, id, name, tur = '{}[{}{}{}] {}{}'.format(bold_merah, bold_putih, str(self.loop), bold_merah, str(target), bold_putih), '{}Not Found'.format(bold_merah), '{}Unknown'.format(bold_merah), 0
        PrintTarget1(tg, id, name)
        return(tur, id)

    def DumpCookie(self, r, Data, tab_key, cursor):
        try:
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','variables':json.dumps({"count":8,"cursor":cursor,"scale":2,"search":None,"id":tab_key}),'server_timestamps':True,'doc_id':'6709724792472394'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    rw = x['node']['actions_renderer']['profile_actions'][0]['client_handler']['profile_action']['restrictable_profile_owner']
                    id, nm, un = str(rw['id']), str(rw['name']), str(x['node']['url']).replace('https://www.facebook.com/','').replace('profile.php?id=','')
                    fm = '{}|{}|{}'.format(id, un, nm)
                    if str(un) != 'None':
                        if SaveResult(self.save_file, fm): self.loopdump += 1
                        print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            if pos['data']['node']['pageItems']['page_info']['has_next_page']:
                end_cursor = pos['data']['node']['pageItems']['page_info']['end_cursor']
                self.DumpCookie(r, Data, tab_key, end_cursor)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def DumpToken(self, r, url, token, resp):
        try:
            for i in resp['data']:
                try:
                    fm = '{}|{}|{}'.format(i['id'], i['id'], i['name'])
                    if SaveResult(self.save_file, fm): self.loopdump += 1
                    print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            after = resp['paging']['cursors']['after']
            new_resp = r.get(url, params={'access_token':token,'after':after,'pretty':'1'}, cookies={'cookie':self.cookie}).json()
            self.DumpToken(r, url, token, new_resp)
        except KeyboardInterrupt: pass
        except Exception as e: pass

#--> Dump Member Group
class DumpGroup():

    def __init__(self, isLogin):
        self.loop = 0
        self.isLogin = isLogin
        self.cookie = CurrentCookies()
        list_target = InputTarget1()
        self.save_file = SaveFile()
        ctrlc()
        for group in list_target:
            self.loop += 1; self.loopdump = 0
            r = requests.Session()
            url = ConvertURL(group).replace('groups/','').replace('www.facebook.com','www.facebook.com/groups')
            try:
                if self.isLogin: req = r.get(url, headers=HeadersGetWindows(), cookies={'cookie':self.cookie}, allow_redirects=True).text.replace('\\','')
                else: req = r.get(url, headers=HeadersGetWindows(), allow_redirects=True).text.replace('\\','')
            except Exception as e: req = 'null'
            id_group, info = self.ShowInfo(group, req)
            if req != 'null' and info == 1 and id_group != 0:
                if self.isLogin: self.LoopDump(r, GetData(req), id_group, None)
                else: self.LoopDumpNoLogin(r, GetDataNoLogin(req), id_group, None)
            print('\rSuccess Dump {} ID'.format(str(self.loopdump)))
            print('')
            r.close()
        FinishFile(self.save_file)

    def ShowInfo(self, target, req):
        try:
            id     = re.search(r'"groupID":"(.*?)"',str(req)).group(1)
            name   = re.search(r'"id":"{}","name":"(.*?)"'.format(id),str(req)).group(1)
            type   = re.search(r'"text":"(.*?)"}},"group_member_profiles"',str(req)).group(1).split('"text":"')[-1]
            join   = re.search(r'"viewer_join_state":"(.*?)"',str(req)).group(1)
            member = re.search(r'"group_member_profiles":{"formatted_count_text":"(.*?)"}',str(req)).group(1).replace('u00a0',' ')
            if (('privat' in str(type).lower()) and (join == 'CAN_REQUEST')): t, a, b, c, d, r = '{}[{}{}{}] {}{}'.format(bold_merah, bold_putih, str(self.loop), bold_merah, str(target), bold_putih), '{}{}'.format(bold_merah, id), '{}{}'.format(bold_merah, name), '{}{}'.format(bold_merah, type), '{}{}'.format(bold_merah, member), 0
            else: t, a, b, c, d, r = '{}[{}{}{}] {}{}'.format(bold_cyan, bold_putih, str(self.loop), bold_cyan, str(target), bold_putih), '{}{}'.format(bold_cyan, id), '{}{}'.format(bold_cyan, name), '{}{}'.format(bold_cyan, type), '{}{}'.format(bold_cyan, member), 1
        except Exception as e: t, a, b, c, d, r, id = '{}[{}{}{}] {}{}'.format(bold_merah, bold_putih, str(self.loop), bold_merah, str(target), bold_putih), '{}ID Group Not Found'.format(bold_merah), '{}Unknown'.format(bold_merah), '{}Unknown'.format(bold_merah), '{}Unknown'.format(bold_merah), 0, 0
        PrintTarget2(t, a, b, c, d)
        return(id, r)

    def LoopDump(self, r, Data, id_group, cursor):
        try:
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupsCometMembersPageNewMembersSectionRefetchQuery','variables':json.dumps({"count":10,"cursor":cursor,"groupID":id_group,"recruitingGroupFilterNonCompliant":False,"scale":2,"id":"804848814300940"}),'server_timestamps':True,'doc_id':'6621621524622624'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['new_members']['edges']:
                try:
                    id, nm, un = str(x['node']['id']), str(x['node']['name']), str(x['node']['url']).replace('https://www.facebook.com/','').replace('profile.php?id=','')
                    fm = '{}|{}|{}'.format(id, un, nm)
                    if str(un) != 'None':
                        if SaveResult(self.save_file, fm): self.loopdump += 1
                        print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            if pos['data']['node']['new_members']['page_info']['has_next_page']:
                end_cursor = pos['data']['node']['new_members']['page_info']['end_cursor']
                self.LoopDump(r, Data, id_group, end_cursor)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def LoopDumpNoLogin(self, r, data, id_group, cursor):
        try:
            var = {"count":3, "cursor":cursor, "feedLocation":"GROUP", "feedType":"DISCUSSION", "feedbackSource":0, "focusCommentID":None, "privacySelectorRenderLocation":"COMET_STREAM", "renderLocation":"group", "scale":2, "sortingSetting":None, "stream_initial_count":1, "useDefaultActor":False, "id":id_group, "__relay_internal__pv__IsWorkUserrelayprovider":False, "__relay_internal__pv__IsMergQAPollsrelayprovider":False, "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False, "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False, "__relay_internal__pv__StoriesRingrelayprovider":False}
            data.update({'fb_api_caller_class':'RelayModern', 'server_timestamps':True, 'fb_api_req_friendly_name':'GroupsCometFeedRegularStoriesPaginationQuery', 'variables':json.dumps(var), 'doc_id':'7224820557637894'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=data).text.replace('\\','')
            list_id_post = list(set(re.findall(r'"share_fbid":"(.*?)"',str(pos))))
            for id_post in list_id_post:
                try:
                    enc_id_post = base64.b64encode(('feedback:{}'.format(id_post)).encode('utf-8')).decode('utf-8')
                    self.Reaction(r, data, enc_id_post)
                    self.Comment(r, data, enc_id_post)
                except KeyboardInterrupt: break
                except Exception as e: continue
            if re.search(r'"has_next_page":(.*?)}',str(pos)).group(1) == 'true':
                next_cursor = re.search(r'"end_cursor":"(.*?)"',str(pos)).group(1)
                self.LoopDumpNoLogin(r, data, id_group, next_cursor)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def Reaction(self, r, data, enc_id):
        for react in ["1635855486666999","1678524932434102","115940658764963","478547315650144","908563459236466","444813342392137","613557422527858"]:
            data.update({'fb_api_caller_class':'RelayModern', 'fb_api_req_friendly_name':'CometUFIReactionIconTooltipContentQuery', 'variables':json.dumps({"feedbackTargetID":enc_id,"reactionID":react}), 'server_timestamps':True, 'doc_id':'6235145276554312'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=data).json()
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for i in pos['data']['feedback']['reactors']['nodes']:
                    TPE.submit(self.Convert, i.get('id'))

    def Comment(self, r, data, enc_id):
        var = {"commentsIntentToken":"CHRONOLOGICAL_UNFILTERED_INTENT_V1","feedLocation":"DEDICATED_COMMENTING_SURFACE","feedbackSource":110,"focusCommentID":None,"scale":2,"useDefaultActor":False,"id":enc_id}
        data.update({'fb_api_caller_class':'RelayModern', 'fb_api_req_friendly_name':'CommentListComponentsRootQuery', 'variables':json.dumps(var), 'server_timestamps':True, 'doc_id':'24724922420456657'})
        pos = r.post('https://www.facebook.com/api/graphql/', data=data).json()
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for i in pos['data']['node']['comment_rendering_instance_for_feed_location']['comments']['edges']:
                TPE.submit(self.Convert, i['node']['author']['id'])

    def Convert(self, raw_id):
        gt = ConvertID(raw_id)
        if (gt['id'] != '0') and ((gt['name']).replace(' ','').isalpha()):
            fm = '{}|{}|{}'.format(gt['id'], gt['username'], gt['name'])
            if SaveResult(self.save_file, fm): self.loopdump += 1
            print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)

#--> Dump React & Comment Post
class DumpPost():

    def __init__(self, isLogin):
        self.cookie = CurrentCookies()
        self.loop = 0
        list_target = InputTarget1()
        self.save_file = SaveFile()
        ctrlc()
        for target in list_target:
            self.loop += 1; self.loopdump = 0
            r = requests.Session()
            url = ConvertURL(target)
            try: req = r.get(url, headers=HeadersGetWindows(), cookies={'cookie':self.cookie}, allow_redirects=True).text.replace('\\','')
            except Exception as e: req = 'null'
            feed, info = self.ShowInfo(target, req)
            if req != 'null' and feed != 'null' and info == 1:
                Data = GetData(req)
                self.LoopDumpComment(r, Data, feed, None, 0)
                self.LoopDumpReact(r, Data, feed, None)
            print('\rSuccess Dump {} ID'.format(str(self.loopdump)))
            print('')
            r.close()
        FinishFile(self.save_file)

    def ShowInfo(self, target, req):
        try:
            feed = re.search(r'"feedback":{"id":"(.*?)"',str(req)).group(1)
            fbi1 = re.search(r'"post_id":"(.*?)"',str(req)).group(1)
            nam1 = re.search(r'"answer_agent_group_id":.*?,"profile_url":\".*?\","name":"(.*?)"',str(req)).group(1)
            tg, fbid, name, tur = '{}[{}{}{}] {}{}'.format(bold_cyan, bold_putih, str(self.loop), bold_cyan, str(target), bold_putih), '{}{}'.format(bold_cyan, fbi1), '{}{}'.format(bold_cyan, nam1), 1
        except Exception as e: tg, feed, fbid, name, tur = '{}[{}{}{}] {}{}'.format(bold_merah, bold_putih, str(self.loop), bold_merah, str(target), bold_putih), 'null', '{}Not Found'.format(bold_merah), '{}Unknown'.format(bold_merah), 0
        PrintTarget1(tg, fbid, name)
        return(feed, tur)

    def LoopDumpReact(self, r, Data, feed, cursor):
        try:
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFIReactionsDialogTabContentRefetchQuery','variables':json.dumps({"count":10,"cursor":cursor,"feedbackTargetID":feed,"reactionID":None,"scale":2,"id":feed}),'server_timestamps':True,'doc_id':'24094105923567748'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['reactors']['edges']:
                try:
                    id, nm, un = str(x['node']['id']), str(x['node']['name']), str(x['node']['url']).replace('https://www.facebook.com/','').replace('profile.php?id=','')
                    fm = '{}|{}|{}'.format(id, un, nm)
                    if str(un) != 'None':
                        if SaveResult(self.save_file, fm): self.loopdump += 1
                        print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            if pos['data']['node']['reactors']['page_info']['has_next_page']:
                end_cursor = pos['data']['node']['reactors']['page_info']['end_cursor']
                self.LoopDumpReact(r, Data, feed, end_cursor)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def LoopDumpComment(self, r, Data, feed, cursor, lop):
        try:
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CommentsListComponentsPaginationQuery','variables':json.dumps({"commentsAfterCount":lop,"commentsAfterCursor":cursor,"commentsBeforeCount":None,"commentsBeforeCursor":None,"commentsIntentToken":"CHRONOLOGICAL_UNFILTERED_INTENT_V1","feedLocation":"PERMALINK","focusCommentID":None,"scale":2,"useDefaultActor":False,"id":feed}),'server_timestamps':True,'doc_id':'6821968557914145'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['comment_rendering_instance_for_feed_location']['comments']['edges']:
                try:
                    id, nm, un = str(x['node']['author']['id']), str(x['node']['author']['name']), str(x['node']['author']['url']).replace('https://www.facebook.com/','').replace('profile.php?id=','')
                    fm = '{}|{}|{}'.format(id, un, nm)
                    if str(un) != 'None':
                        if SaveResult(self.save_file, fm): self.loopdump += 1
                        print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            if pos['data']['node']['comment_rendering_instance_for_feed_location']['comments']['page_info']['has_next_page']:
                end_cursor = pos['data']['node']['comment_rendering_instance_for_feed_location']['comments']['page_info']['end_cursor']
                self.LoopDumpComment(r, Data, feed, end_cursor, lop-1)
        except KeyboardInterrupt: pass
        except Exception as e: pass

#--> Dump Nama
class DumpName():

    def __init__(self, isLogin):
        self.isLogin = isLogin
        self.cookie = CurrentCookies()
        self.loopdump = 0
        list_nama = InputTarget2()
        self.save_file = SaveFile()
        ctrlc()
        for nama in list_nama:
            try:
                r = requests.Session()
                list_name = self.GenerateName(r, nama)
                r.close()
                for name in list_name:
                    try:
                        rr  = requests.Session()
                        if self.isLogin:
                            req = rr.get('https://www.facebook.com/search/people/?q={}'.format(name), headers=HeadersGetWindows(), cookies={'cookie':self.cookie}).text.replace('\\','')
                            bsid = re.search(r'"bsid":"(.*?)"',str(req)).group(1)
                            self.LoopDump(rr, GetData(req), bsid, None, name)
                        else:
                            req = rr.get('https://m.facebook.com/public/{}'.format(name), headers=HeadersGetAndroid()).text.replace('\\','')
                            self.LoopDumpNoLogin(rr, req)
                        rr.close()
                    except KeyboardInterrupt: break
                    except Exception as e: continue
            except KeyboardInterrupt: break
            except Exception as e: continue
        FinishFile(self.save_file)

    def GenerateName(self, r, name):
        daftar_nama, sementara = [], []
        daftar_nama.append(name)
        url = 'http://ninjaname.net/indonesian_name.php'
        try:
            pos = r.post(url, data={'number_generate':'50','gender_type':random.choice(['male','female']),'submit':'Generate'}).text.replace('\\','')
            xd = re.findall(r'bull; (.*?)<br/>',str(pos))
            for i in xd:
                for j in i.split(' '):
                    if j not in sementara: sementara.append(j)
            for k in sementara: daftar_nama.append('{}+{}'.format(name,k))
        except Exception as e: pass
        return(daftar_nama)

    def LoopDump(self, r, Data, bsid, cursor, name):
        try:
            Var = {"UFI2CommentsProvider_commentsKey":"SearchCometResultsInitialResultsQuery","allow_streaming":False,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":False,"high_confidence_config":None,"intercept_config":None,"sts_disambiguation":None,"watch_config":None},"context":{"bsid":bsid,"tsid":None},"experience":{"encoded_server_defined_params":None,"fbid":None,"type":"PEOPLE_TAB"},"filters":[],"text":name.replace('+',' ')},"count":5,"cursor":cursor,"displayCommentsContextEnableComment":False,"displayCommentsContextIsAdPreview":False,"displayCommentsContextIsAggregatedShare":False,"displayCommentsContextIsStorySet":False,"displayCommentsFeedbackContext":None,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":True,"focusCommentID":None,"locale":None,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":2,"stream_initial_count":0,"useDefaultActor":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'SearchCometResultsPaginatedResultsQuery','variables':json.dumps(Var),'server_timestamps':True,'doc_id':'7260455920683280'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            if 'CRITICAL' in str(pos) and 'Rate limit exceeded' in str(pos): exit(Spam())
            for x in pos['data']['serpResponse']['results']['edges']:
                try:
                    rw = x['relay_rendering_strategy']['view_model']['profile']
                    id, nm, un = str(rw['id']), str(rw['name']), str(rw['url']).replace('https://www.facebook.com/','').replace('profile.php?id=','')
                    fm = '{}|{}|{}'.format(id, un, nm)
                    if str(un) != 'None':
                        if SaveResult(self.save_file, fm): self.loopdump += 1
                        print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
                except Exception as e: continue
            if pos['data']['serpResponse']['results']['page_info']['has_next_page']:
                end_cursor = pos['data']['serpResponse']['results']['page_info']['end_cursor']
                self.LoopDump(r, Data, bsid, end_cursor, name)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def LoopDumpNoLogin(self, r, response):
        try:
            list_id = list(set(re.findall(r'href="fb://profile/\?id=(.*?)&',str(response))))
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for id in list_id:
                    TPE.submit(self.Convert, id)
            next = re.search(r'"see_more_pager",href:"(.*?)"',str(response)).group(1)
            response = r.get(next, headers=HeadersGetAndroid()).text.replace('\\','')
            self.LoopDumpNoLogin(r, response)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def Convert(self, raw_id):
        gt = ConvertID(raw_id)
        if (gt['id'] != '0') and ((gt['name']).replace(' ','').isalpha()):
            fm = '{}|{}|{}'.format(gt['id'], gt['username'], gt['name'])
            if SaveResult(self.save_file, fm): self.loopdump += 1
            print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)

#--> Dump Random ID
class DumpRandomID():

    def __init__(self, isLogin):
        self.loopdump = 0
        self.save_file = SaveFile()
        self.Ask()

    def Ask(self):
        try: years = [int(i) for i in input('{}Akun Tahun Berapa : {}'.format(bold_putih, bold_cyan)).replace(' ','').split(',')]
        except Exception as e: exit('{}Anda Harus Menulis Angka Yang Benar!{}\n'.format(bold_merah, bold_putih))
        ctrlc()
        print('\r{}'.format(bold_putih), end='')
        for i in years: self.SortID(i)

    def SortID(self, years):
        years_based = {
            2024:['61550','61551','61552','61553','61554','61555','61556'],
            2023:['10009'],
            2022:['10008'],
            2021:['10006','10007'],
            2020:['10005'],
            2019:['10004'],
            2018:['10003'],
            2017:['10002'],
            2016:['10001'],
            2015:['100007','100008','100009'],
            2014:['100005','100006'],
            2013:['100004'],
            2012:['100003'],
            2011:['100002'],
            2010:['100001','1000006','1000007','1000008','1000009'],
            2009:['18','19','100000','1000001','1000002','1000003','1000004','1000005','1000000']}
        front = years_based.get(years)
        if front is None : exit('{}Tahun Harus Berada Direntang 2009-2024!{}\n'.format(bold_merah, bold_putih))
        else:
            self.limiter = 0
            with ThreadPoolExecutor(max_workers=30) as TPE:
                while(True):
                    try:
                        front_digit = random.choice(front)
                        if (front_digit[:2] == '61'): id = '{}{}'.format(str(front_digit), str(random.randrange(100000000,1000000000)))
                        elif len(str(front_digit)) == 2: id = '{}{}'.format(str(front_digit), str(random.randrange(10000000,100000000)))
                        else: id = '{}{}'.format(str(front_digit), str(random.randrange(10**(14-len(str(front_digit))),10**(15-len(str(front_digit))))))
                        TPE.submit(self.Convert, id)
                    except KeyboardInterrupt: break
                    except Exception as e: continue

    def Convert(self, raw_id):
        gt = ConvertID(raw_id)
        if (gt['id'] != '0') and ((gt['name']).replace(' ','').isalpha()):
            fm = '{}|{}|{}'.format(gt['id'], gt['username'], gt['name'])
            if SaveResult(self.save_file, fm): self.loopdump += 1
            print('\rSuccess Dump {} ID'.format(str(self.loopdump)), end='', flush=True)
            self.limiter += 1

#--> Dump Email
class DumpEmail():

    def __init__(self, isLogin):
        self.cookie = CurrentCookies()
        self.HeadersPost = {'Host':'www.facebook.com','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?0','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Viewport-Width':'1280','Content-Type':'application/x-www-form-urlencoded','Sec-Ch-Ua-Platform-Version':'','X-Asbd-Id':'129477','Dpr':'1.25','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Model':'','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua-Platform':'','Accept':'*/*','Origin':'https:/www.facebook.com','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https:/www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Priority':'u=1, i'}
        self.SortEmail()

    def SortEmail(self):
        target = 'joko'
        domain = 'gmail.com'
        list_email = ['{}{}@{}'.format(target, i, domain) for i in range(10,5000)]
        # list_email = ['hanastarayartha@gmail.com']
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for email in list_email:
                TPE.submit(self.GetData, email)

    def GetData(self, email):
        try:
            r = requests.Session()
            req = r.get('https://mbasic.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0').text.replace('\\','').replace('amp;','')
            data = {'jazoest':re.search(r'name="jazoest" value="(.*?)"',str(req)).group(1),'lsd':re.search(r'name="lsd" value="(.*?)"',str(req)).group(1),'email':email,'did_submit':'Cari'}
            url = 'https://mbasic.facebook.com{}'.format(re.search(r'action="(.*?)"',str(req)).group(1))
            pos = r.post(url, data=data).text.replace('\\','').replace('amp;','')
            nama = re.search(r'<strong><strong>(.*?)</strong></strong>',str(pos)).group(1)
            fm = '{}|{}'.format(email, nama)
            print(fm)
            r.close()
        except Exception as e: pass

#--> Dump Nomor Telepon
class DumpPhone():

    def __init__(self, isLogin):
        self.cookie = CurrentCookies()