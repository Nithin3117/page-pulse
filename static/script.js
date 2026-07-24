const button = document.getElementById("analyzeBtn");
button.addEventListener("click", async () => {
    const url = document.getElementById("urlInput").value.trim();
    const result = document.getElementById("result");
    const errorBox = document.getElementById("errorBox");
    const loading = document.getElementById("loading");
    result.style.display = "none";
    errorBox.style.display = "none";
    if (!url) {
        errorBox.textContent = "Please enter a website URL.";
        errorBox.style.display = "block";
        return;
    }
    button.disabled = true;
    button.textContent = "Analyzing...";
    loading.style.display = "block";
    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                url: url
            })
        });
        const data = await response.json();
        loading.style.display = "none";
        if (data.error) {
            errorBox.textContent = data.error;
            errorBox.style.display = "block";
        } else {
            result.style.display = "block";
            document.getElementById("status").textContent = data.http_status;
            document.getElementById("time").textContent = data.response_time;
            document.getElementById("title").textContent = data.title;
            document.getElementById("meta").textContent = data.meta_description;
            document.getElementById("h1").textContent = data.h1_count;
            document.getElementById("alt").textContent = data.missing_alt_images;
            document.getElementById("words").textContent = data.word_count;
        }
    } catch (error) {
        loading.style.display = "none";
        errorBox.textContent = "Unable to connect to the server.";
        errorBox.style.display = "block";
    } finally {
        button.disabled = false;
        button.textContent = "Analyze";
    }
});
