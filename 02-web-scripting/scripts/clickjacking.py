""" Clickjacking scanner 
=================================

just a practice script 
"""

import sys #commind line se arguement
import requests
from dataclasses import dataclass #for data handling 
from functools import wraps # python helper
import time


#========================================
# concept 1 : Decorators
#========================================

# concept used : decorators with parameters,
# what is does print time stamp before or after functions runs
# __name__ is the attribute of function, in python journly everything has __name__ attribute

# but we need to add a helper here @wraps(func)
# if we dont then

""""@log_step          ← this decorator  on fetch_headers 
def fetch_headers(): ...
                   ↓
fetch_headers = log_step(fetch_headers)
                   ↓
fetch_headers now automatically is wrapper,
LEKIN wraps ki wajah se apna naam "fetch_headers" batata hai

means if we dont add helper wrap then its will show name wrapper
"""



def log_step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} start....")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} finished")
        return result
    return wrapper


## concept 2: dataclss use 

@dataclass
class ScanResult:
    #becuase of data classs
    target:str
    xfo_present:bool
    csp_frame_present:bool
    vulnerable:bool
    detail:str


    def summary(self):
        status = "vulnerable " if self.vulnerable else "safe"
        return(
            f"clickjacking scan result\n"
            f"target: {self.target}\n"
            f"x-frame-options : {'yes' if self.xfo_present else 'no'}\n"
            f"CSP frame-ancestors: {'YES' if self.csp_frame_present else 'NO'}\n"
            f"Status: {status}\n"
            f"Detail: {self.detail}\n"
        )


# dataclass adecorator automatically makes __init__
# with default values true

# agar dataclass use na krein to 


"""class ScanResult:
    def __init__(self, target, xfo_present, csp_frame_present, vulnerable, detail):
        self.target = target
        self.xfo_present = xfo_present
        self.csp_frame_present = csp_frame_present
        self.vulnerable = vulnerable
        self.detail = detail"""



# concept 3: lets make object and manage state


class ClickjackingScanner:

    SAFE_XFO_VALUES = {"deny","sameorigin"}


    def __init__(self,target_url):
        # self refer current object
        self.target = target_url
        self.session = requests.session()
        self.session.headers.update({
            "User-Agent" : "Mozila-firefox/5.0"
        })

    @log_step
    def fetch_headers(self):
        try:
            response = self.session.get(self.target, timeout=10)
            #convert headers to lower case 
            return{k.lower(): v for k, v in response.headers.items()}
        except requests.RequestException as e:
            print(f"request fail : {e}")
            return None

    @log_step
    def analyze(self, headers):
        # decide if vulnerable or safe
        if headers is None:
            return ScanResult(
                target=self.target,
                xfo_present=False,
                csp_frame_present=False,
                vulnerable=True,
                detail="not able toconnect"
            )

        # check 1: x frame options

        xfo = headers.get("x-frame-options","")
        xfo_safe = xfo.lower() in self.SAFE_XFO_VALUES

        # Check 2: CSP frame-ancestors directive
        csp = headers.get("content-security-policy", "")
        csp_frame_safe = "frame-ancestors" in csp.lower()

        # Final verdict
        is_vulnerable = not (xfo_safe or csp_frame_safe)

        # Detail message
        if is_vulnerable:
            detail = "Dono protection missing — iframe se attack possible"
        elif xfo_safe and not csp_frame_safe:
            detail = "X-Frame-Options active, CSP missing (legacy protection)"
        elif csp_frame_safe and not xfo_safe:
            detail = "CSP frame-ancestors active (modern protection)"
        else:
            detail = "Dono protections active (best practice)"

        

        return ScanResult(
            target=self.target,
            xfo_present=bool(xfo_safe),
            csp_frame_present=csp_frame_safe,
            vulnerable=is_vulnerable,
            detail=detail,
        )

    def run(self):
        """Main entry point — sab kuch yahan se trigger hota hai."""
        print(f"\n[*] Scanning: {self.target}")
        headers = self.fetch_headers()
        result = self.analyze(headers)
        print(result.summary())
        return result



# ======
# CONCEPT 4: if __name__ == "__main__" 
# ==============================
if __name__ == "__main__":
    # User ne URL
    if len(sys.argv) < 2:
        print("Usage: python clickjacking_scanner.py <URL>")
        print("Example: python clickjacking_scanner.py https://example.com")
        sys.exit(1)

    target = sys.argv[1]
    if not target.startswith("http"):
        target = "https://" + target

    
    scanner = ClickjackingScanner(target)
    result = scanner.run()

    # Exit code — 0 = safe, 1 = vulnerable (useful for automation)
    sys.exit(1 if result.vulnerable else 0)

