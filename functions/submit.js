export async function onRequestPost(context) {
  try {
    const data = await context.request.formData();
    const name = data.get("name");
    const email = data.get("email");
    const message = data.get("message");

    // 🔑 Replace with your real SendGrid API key
    const SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY";

    const resp = await fetch("https://api.sendgrid.com/v3/mail/send", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${SENDGRID_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        personalizations: [{ to: [{ email: "jlpaving.org@gmail.com" }] }],
        from: { email: "no-reply@jlpavingwv.com" },
        subject: "New Contact Form Submission",
        content: [
          { type: "text/plain", value: `From: ${name} <${email}>\n\n${message}` }
        ]
      })
    });

    if (!resp.ok) throw new Error(await resp.text());
    return new Response("Form submitted!", { status: 200 });
  } catch (err) {
    return new Response("Error submitting form: " + err.message, { status: 500 });
  }
}
