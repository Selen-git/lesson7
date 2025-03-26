#1:

import org.openqa.selenium.By;
import org.openqa.selenium.Webdriver;

public class CalculatorPage {
    private Webdriver driver;

    public CalculatorPage(WebDriver driver) {
        this.driver = driver;
    }

    private By delayInput = By.id("delay");
    private By resultOutput = By.id("result");

    private By calculatorButton(String Button) {
        return By.xpath("//button[text()='" + button + "']");
    }

    public void enterDelay(String delay) {
        driver.findElement(delayInput).sendKeys(delay);
    }

    public void clickCalculatorButton(String button) {
        driver.findElement(calculatorButton(button)).click();
    }

    public String getResult() {
        return driver.findElement(resultOutput).getText();
    }
}





import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testing.annotations.AfterClass;
import org.testing.annotations.BeforeClass;
import org.testing.annotations.Test;

public class CalculatorTest {
    private WebDriver driver;
    private CalculatorPage calculatorPage;

    @BeforeClass
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
        calculatorPage = new CalculatorPage(driver);
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html");
    }

    @Test
    public void testCalculator() {
        calculatorPage.enterDelay("1000");
        calculatorPage.clickCalculatorButton("1");
        calculatorPage.clickCalculatorButton("+");
        calculatorPage.clickCalculatorButton("2");
        calculatorPage.clickCalculatorButton("=");
        String result = calculatorPage.getResult();
        System.out.printIn("Result: " + result);
    }


    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}









#2:

public class CalculatorPage {
    private WebDriver driver;

    private By delayInput = By.cssSelector("#delay");
    private By button7 = By.cssSelector("#button7");
    private By buttonPlus = By.cssSelector("#buttonPlus");
    private By button8 = By.cssSelector("#button8");
    private By buttonEquals = By.cssSelector("#buttonEquals");
    private By resultWindow = By.cssSelector("#result");

    public calculatorPage(WebDriver driver) {
        this.driver = driver;
    }

    public void setDelay(String value) {
        driver.findElement(delayInput).sendKeys(value);
    }

    public void clickButton7() {
        driver.findElement(button7).click();
    }

    public void clickButtonPlus() {
        driver.findElement(buttonPlus).click();
    }


    public void clickButton8() {
        driver.findElement(button8).click();
    }


    public void clickButtonEquals() {
        driver.findElement(buttonEquals).click();
    }

    public String getResult() {
        return driver.findElement(resultWindow).getText();
    }
}



public class CalculatorTest {
    private WebDriver driver;
    private CalculatorPage calculatorPage;

    @Before
    public void setUp() {
        System.setProperty("webdriver.chrome.driver", "path_to_chromedriver");
        driver = new ChromeDriver();
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html");
        calculatorPage = new CalculatorPage(driver);
    }

    @Test
    public void testSlowCalculator() {
        calculatorPage.setDelay("45");
        calculatorPage.clickButton7();
        calculatorPage.clickButtonPlus();
        calculatorPage.clickButton8();
        calculatorPage.clickButtonEquals();

        WebDriverWait wait = new WebDriverWait(driver, 45);
        wait.until(ExpectedConditions.visibilityofElementLocated(By.cssSelector("#result")));

        assertEquals("15", calculatorPage.getResult());
    }

    @After
    public void tearDown() {
        driver.quit();
    }
}













