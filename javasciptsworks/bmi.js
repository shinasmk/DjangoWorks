var height=165

var weight=82

var heightInMeter=height/100

var bmi=weight/(heightInMeter**2)

if (bmi<18.5){
    console.log("underweight");
}
else if(bmi>=18.5 && bmi<24.9){
    console.log("healthy Weight");
}
else if(bmi>25 && bmi<29.9){
    console.log("overweight");
}
else{
    console.log("obesity")
}
