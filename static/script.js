async function uploadPDFs() {
    const files = document.getElementById("pdfs").files;

    const formData = new FormData();

    for (let file of files) {
        formData.append("files", file);
    }

    await fetch("/upload", {
        method: "POST",
        body: formData
    });

    alert("PDFs uploaded");
}

async function sendMessage() {
    const message = document.getElementById("message").value;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    document.getElementById("chat").innerHTML += `
        <p><b>You:</b> ${message}</p>
        <p><b>Bot:</b> ${data.answer}</p>
    `;
}
