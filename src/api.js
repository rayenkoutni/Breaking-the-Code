export async function analyzeCiphertext(ciphertext) {
  const response = await fetch("http://localhost:5000/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ ciphertext })
  });

  if (!response.ok) {
    throw new Error("Analysis failed");
  }

  return response.json();
}
