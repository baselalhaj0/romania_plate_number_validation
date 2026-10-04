import cloudscraper, time, requests
from colorama import Fore, Back, init
from anticaptchaofficial.recaptchav2proxyless import *
init(convert=True)


with open("numere.txt", "r") as f:
    listanr = [line.strip() for line in f]

i = 0
while(i<=len(listanr)-1):
    numar = listanr[i]
    i+=1
    solver = recaptchaV2Proxyless()
    solver.set_key("37bca02c35a7f55e10960dee93ebe006")  # API Key anticaptcha
    solver.set_website_url("https://dgpci.mai.gov.ro/drpciv-forms/plate-number")
    solver.set_website_key("6Le9UwsUAAAAAGR_XRglppXV_ZTRjQOcPPyz7dxA")  # sitekey extras
    
    token = solver.solve_and_return_solution()
    
    sc = cloudscraper.create_scraper(
        captcha={
        'provider': 'anticaptcha',
        'api_key': '37bca02c35a7f55e10960dee93ebe006'
      })
    
    if token !=0:
        try:
            headers = {
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.9,ro;q=0.8",
                "content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
            }
            
            payload = {
                "language": "RO",
                "plateNumber": numar,
                "userEmail" : "",
                "reCaptchaKey" : token
                }
            
            r = sc.post("https://dgpci.mai.gov.ro/drpciv-forms-api/plate-status", json=payload, headers=headers)
            if '"code":"available"' in r.text:
                print(f"{Fore.GREEN}{numar}{Fore.WHITE}")
            elif '"code":"not-available"' in r.text:
                print(f"{Fore.RED}{numar}{Fore.WHITE}")
            elif "Codul captcha este invalid!" in r.text:
                print(f"{Fore.YELLOW}{numar}{Fore.WHITE}")
                i-=1
            else:
                print(r.text + numar)
                i-=1
    
        except:
            print(F"NU S-A PUTUT VERIFICA NUMARUL : {numar}")
            i-=1
    else:
        print(F"NU S-A PUTUT VERIFICA NUMARUL : {numar}")
        i-=1


