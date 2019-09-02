# sendtimemin: 20
# sendtimehour: 18
# sendtimeday: 19
# sendtimemonth: 7
# sendtimeyear: 2019
# 795c94b9585b0e527f255d6e019fccc1: a8856fe0f9b57f51e842689a6c6d53da
# sid: Zm_tSR6VwNfm72wx
# from_s: cnew
# to: 762741385@qq.com            ########
# subject: asd                  #########
# content__html: <div>adasdasd737392044</div>   ##########
# sendmailname: 2199344905@qq.com    ######
# savesendbox: 1
# actiontype: send
# sendname: 鱼                  ########
# acctid: 0
# separatedcopy: false
# s: comm
# hitaddrbook: 0
# selfdefinestation: -1
# domaincheck: 0
# cgitm: 1563528131080                  33333333333
# clitm: 1563528130327           ######
# comtm: 1563528241418          ##########
# logattcnt: 0
# logattsize: 0
# cginame: compose_send
# ef: js
# t: compose_send.json
# resp_charset: UTF8

# 795c94b9585b0e527f255d6e019fccc1: a8856fe0f9b57f51e842689a6c6d53da
# sid: Zm_tSR6VwNfm72wx
# from_s: cnew
# to: 15858102962@163.com
# subject: fgfg
# content__html: <div>fgfdddg</div>
# sendmailname: 2199344905@qq.com
# savesendbox: 1
# actiontype: send
# sendname: 鱼
# acctid: 0
# separatedcopy: false
# s: comm
# hitaddrbook: 0
# selfdefinestation: -1
# domaincheck: 0
# cgitm: 1563528131080
# clitm: 1563528130327
# comtm: 1563528410349
# logattcnt: 0
# logattsize: 0
# cginame: compose_send
# ef: js
# t: compose_send.json
# resp_charset: UTF8
import random
import time

import requests


def send_qq_email(s_id, to_user, email_subject, email_content):
    header = {
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'RK=vHZRPHQ5RC; ptcz=19e2a6c0aac928cb16a5133ccf795e575699a4fa8fb96ab35d494d7e5b0e05f5; pgv_pvid=1060514191; qm_logintype=qq; edition=mail.qq.com; pgv_pvi=8041609216; pgv_si=s1114263552; ptisp=; ptui_loginuin=2199344905; uin=o2199344905; skey=@BLrE2QQb3; p_uin=o2199344905; pt4_token=5wVVZDJ7CEF3iWyiUwP9OSi-Ayvjhj5jJCrrJyrbcv4_; p_skey=XZJ974-08jzmRHQ*rtcb72rzuGzKato4gt4390ZVrqY_; wimrefreshrun=0&; qm_flag=0; qqmail_alias=2199344905@qq.com; sid=-2095622391&a8856fe0f9b57f51e842689a6c6d53da,qWFpKOTc0LTA4anptUkhRKnJ0Y2I3MnJ6dUd6S2F0bzRndDQzOTBaVnJxWV8.; qm_username=2199344905; qm_domain=https://mail.qq.com; qm_ptsk=-2095622391&@BLrE2QQb3; foxacc=-2095622391&0; ssl_edition=sail.qq.com; qm_loginfrom=-2095622391&wpt; username=-2095622391&2199344905; pcache=734066756b5625eMTU2NjEyMDEzMA@2199344905@0; CCSHOW=000001; webp=1; new_mail_num=-2095622391&0; qm_authimgs_id=1; qm_verifyimagesession=h015dc1737482f3b69212bd6e10bb83e9b7ff2e7ade5fa7ceb877e9829078b15dc2a270d862d2af8d8e',
        'cookie': 'RK=vHZRPHQ5RC; ptcz=19e2a6c0aac928cb16a5133ccf795e575699a4fa8fb96ab35d494d7e5b0e05f5; pgv_pvid=1060514191; qm_logintype=qq; edition=mail.qq.com; pgv_pvi=8041609216; CCSHOW=000001; webp=1; wimrefreshrun=0&; qm_flag=0; qm_domain=https://mail.qq.com; pgv_si=s6989766656; ptisp=; new_mail_num=-2095622391&0|762741385&0; foxacc=-2095622391&0|762741385&0; ptui_loginuin=2199344905; uin=o2199344905; skey=@0gJMcaJkk; p_uin=o2199344905; pt4_token=wSQuhn23mng0oQ4vsREtxiRzBTLkVBNmNUyjxp3KuYg_; p_skey=Dy2astqCgRA*MfzNdnxu*duaoUnDqHX-2-4Z5X3j2zw_; qqmail_alias=2199344905@qq.com; sid=-2095622391&cb05ce5c6e951821c8e9d094a25db4ba,qRHkyYXN0cUNnUkEqTWZ6TmRueHUqZHVhb1VuRHFIWC0yLTRaNVgzajJ6d18.; qm_username=2199344905; qm_lg=qm_lg; qm_ptsk=-2095622391&@0gJMcaJkk; ssl_edition=sail.qq.com; qm_loginfrom=-2095622391&wpt|762741385&psaread; username=-2095622391&2199344905',
        'origin': 'https://mail.qq.com',
        'pragma': 'no-cache',
        'referer': 'https://mail.qq.com/zh_CN/htmledition/ajax_proxy.html?mail.qq.com&v=140521',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    form_data = {
        '795c94b9585b0e527f255d6e019fccc1': 'a8856fe0f9b57f51e842689a6c6d53da',
        'sid': 'Zm_tSR6VwNfm72wx',
        'from_s': 'cnew',
        'to': '15858102962@163.com',
        'subject': 'fgfg',
        'content__html': '<div>fgfdddg</div>',
        'sendmailname': '2199344905@qq.com',
        'savesendbox': '1',
        'actiontype': 'send',
        'sendname': '鱼',
        'acctid': '0',
        'separatedcopy': 'false',
        's': 'comm',
        'hitaddrbook': '0',
        'selfdefinestation': '-1',
        'domaincheck': '0',
        'logattcnt': '0',
        'logattsize': '0',
        'cginame': 'compose_send',
        'ef': 'js',
        't': 'compose_send.json',
        'resp_charset': 'UTF8',
    }

    url = 'https://mail.qq.com/cgi-bin/compose_send?sid=%s' % s_id

    form_data['sid'] = s_id
    form_data['subject'] = email_subject
    content = '<div>%s</div>' % email_content
    form_data['content__html'] = content
    form_data['clitm'] = int(round(time.time() * 1000))
    form_data['cgitm'] = int(round(time.time() * 1000))
    form_data['comtm'] = int(round(time.time() * 1000))

    for user in to_user:

        form_data['to'] = user

        try:
            res = requests.post(url=url, data=form_data, headers=header)
            print(res.cookies)
            print(res.content)
            status = res.status_code
            if status != 200:
                print("向%s发送失败" % user)
                continue
        except Exception as e:
            print("向%s发送失败" % user, e)
            continue
        print("向%s发送成功" % user)
        time.sleep(random.randint(200, 1200) / 1000)


if __name__ == '__main__':
    sid = 'jof-XAtq28z_khFM'
    # sid = 'Zm_tSR6VwNfm72wx'
    # 737392044
    to = ['762741385@qq.com', '15858102962@163.com']
    subject = 'myj'
    content__html = 'akdjakdjaskldjkl'

    send_qq_email(s_id=sid, to_user=to, email_subject=subject, email_content=content__html)
