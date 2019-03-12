

function check() {
    res = document.getElementById("one");
    res1 = document.getElementById("patientid");
    //alert("/getdoctorname/?department="+res.value+'&'+'patientid='+res1.value);
    window.location.href = "/getdoctorname/?department="+res.value+'&'+'patientid='+res1.value;
}