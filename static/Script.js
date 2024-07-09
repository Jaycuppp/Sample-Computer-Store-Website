// Sample Arr Display Logic
const arr1 = [2, 4, 6];
const arr2 = [3, 5, 7];

console.log([...arr1], [...arr2])

// All Web Page Logic
console.log("Greetings Web User. Welcome to the Official Quansh Tech Website. This JS Page is currently under construction.")

// Home Web Page Logic


function Image_Resizer(Image_Var, Height_Pixels = "", Width_Pixels = "") {
    Image_Var.style.height = Height_Pixels;
    Image_Var.style.width = Width_Pixels;
    return 0
}

// For Resizing Slide Shows Images on HomePage
var HomeSS1 = document.getElementById('SS1'); var HomeSS2 = document.getElementById('SS2');
var HomeSS3 = document.getElementById('SS3'); var HomeSS4 = document.getElementById('SS4');
var HomeSS5 = document.getElementById('SS5'); var HomeSS6 = document.getElementById('SS6');

const Slide_Show_Pics = [HomeSS1, HomeSS2, HomeSS3, HomeSS4, HomeSS5, HomeSS6];

Image_Resizer(Slide_Show_Pics[0], '1000px', '1920px'); Image_Resizer(Slide_Show_Pics[1], '1000px', '1920px');
Image_Resizer(Slide_Show_Pics[2], '1000px', '1920px'); Image_Resizer(Slide_Show_Pics[3], '1000px', '1920px');
Image_Resizer(Slide_Show_Pics[4], '1000px', '1920px'); Image_Resizer(Slide_Show_Pics[5], '1000px', '1920px');


// For Resizing Crypto Images on HomePage 
var BTCPic = document.getElementById('BTC_Logo_Pic'); var ETHPic = document.getElementById('ETH_Logo_Pic');
var SOLPic = document.getElementById('SOL_Logo_Pic'); var USDTPic = document.getElementById('USDT_Logo_Pic');

const Crypto_Currency_Logo = [BTCPic, ETHPic, SOLPic, USDTPic];

Image_Resizer(Crypto_Currency_Logo[0], "200px", "200px"); Image_Resizer(Crypto_Currency_Logo[1], "200px", "275px");
Image_Resizer(Crypto_Currency_Logo[2], "200px", "200px"); Image_Resizer(Crypto_Currency_Logo[3], "200px", "200px")



// Navbar Logic


// Toast Activation Logic
const toastTrigger = document.getElementById('liveToastBtn')
const toastLiveExample = document.getElementById('liveToast')

if (toastTrigger) {
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    toastTrigger.addEventListener('click', () => {
        toastBootstrap.show()
    })
}



// All Product Menu Web Page

var Product_Menu_Image = document.getElementById('All_Products_Image');

Image_Resizer(Product_Menu_Image, "200px", "200px")


function All_Product_Page_Repadding() {
    var Product_Image = document.getElementById('All_Products_Image')
    // Initialize the Condition for when the Product Image is shorter than 280px in Height
    // Based off the Conditions, Add Extra Padding/Margins on the Product Images so it all looks nicer
}

function Pagination_Indicator() {
    var Pagination_Element = document.getElementById('Total_Pages')
    Pagination_Element.classList.add('active')
    // Alter the Styling (CSS) to have the current Page Number from the Pagination be a Very Dark White / Gray color
}