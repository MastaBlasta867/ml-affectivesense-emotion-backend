xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("system_response").innerHTML = xhttp.responseText;
    }
};

xhttp.open("POST", "https://pomolefe-9000.theiadockernext-1-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/analyze", true);
xhttp.setRequestHeader("Content-Type", "application/json");
xhttp.send(JSON.stringify({ text: textToAnalyze }));


