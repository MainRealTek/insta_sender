from requests import Session 
class GetReq(object):
    def __init__(self,user_agent=str(),proxy=True,proxy_type=True,ip_p=str(),user_p=str(),pasw_p=str(),port_p=int()) -> None:
        self.req = Session()
        self.proxy = proxy
        self.proxy_type = proxy_type
        self.user_agent = user_agent
        self.ip_p = ip_p
        self.user_p = user_p
        self.pasw_p = pasw_p
        self.port_p = port_p

        self.req.headers.update ({'Connection' : 'close',
                                'Accept' : '*/*',
                                'Content-type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                                'Cookie2' : '$Version=1',
                                'Accept-Language' : 'en-US',
                                'User-Agent' : self.user_agent,
                                #'Cache-Control' : 'no-cache',
                                'X-Requested-With' :'XMLHttpRequest'})

    def getreq_get(self,url):
        if self.proxy == True:
            if self.proxy_type == True:#http
                self.proxy_statement = {'http' : 'http://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }
            if self.proxy_type == False:#sock5
                self.proxy_statement = {'socket5' : 'socket5://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }
            status = self.req.get(url=url,proxies=self.proxy_statement)
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                #self.req.close()
                return status#,traffic
        if self.proxy != True:
            status = self.req.get(url=url)
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                #self.req.close()
                return status#,traffic
            
    def getreq_post(self,url,header,data):
        if self.proxy == True:
            if self.proxy_type == True:#http
                self.proxy_statement = {'http' : 'http://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }
            if self.proxy_type == False:#sock5
                self.proxy_statement = {'socket5' : 'socket5://{}:{}@{}:{}'.format(self.user_p,self.pasw_p,self.ip_p,self.port_p) }
            status = self.req.post(url=url,proxies=self.proxy_statement,headers=header,data=data)
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                #self.req.close()
                return status#,traffic
        if self.proxy != True:
            status = self.req.post(url=url,data=data)
            traffic = len(status.content) / 1024
            #print(traffic)
            if status.status_code == int(200):
                #self.req.close()
                return status#,traffic

    def close_conn(self):
        self.req.close()
        return True


