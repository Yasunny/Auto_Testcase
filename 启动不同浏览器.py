from selenium import webdriver
import class

public class SeleniumDriver {
    
    private Log log=new Log(this.getClass());
    
    private WebDriver driver;
    
    public WebDriver getDriver() {
        return driver;
    }

    public SeleniumDriver(){
        this.initialDriver();
    }
    
    public void initialDriver(){
        if("firefox".equals(Config.browser)){
            ProfilesIni allProfiles = new ProfilesIni(); 
            FirefoxProfile profile = allProfiles.getProfile("default");
            System.setProperty("webdriver.firefox.bin", "D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe");
            driver = new FirefoxDriver();
        }else if("ie".equals(Config.browser)){
            System.setProperty("webdriver.ie.driver", "files/IEDriverServer64.exe");
            DesiredCapabilities capabilities = DesiredCapabilities.internetExplorer();
            capabilities.setCapability(InternetExplorerDriver.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS, true);
            capabilities.setCapability("ignoreProtectedModeSettings",true);       
            driver = new InternetExplorerDriver(capabilities);
        }else if("chrome".equals(Config.browser)){
            System.setProperty("webdriver.chrome.driver", "files/chromedriver.exe");
            ChromeOptions options = new ChromeOptions();
            options.addArguments("--test-type");
            driver = new ChromeDriver(options);
        }else{    
            log.info(Config.browser+" 的值不正确，请检查！");
            throw new DefinedException(Config.browser+" 的值不正确，请检查！");
        }
    }
