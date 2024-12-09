// // وظيفة لإرسال الرسالة وعرضها في واجهة الدردشة
// function sendMessage() {
//     let userInput = document.getElementById('user-input').value;  // الحصول على مدخلات المستخدم
//     if(userInput.trim() !== "") {
//         // إضافة الرسالة المدخلة من المستخدم
//         document.getElementById('chatbox').innerHTML += "<p><strong>أنت:</strong> " + userInput + "</p>";

//         // مسح المدخلات بعد الإرسال
//         document.getElementById('user-input').value = '';

//         // إضافة إجابة من الشات بوت
//         let botResponse = generateResponse(userInput);  // يمكن تحسين هذه الوظيفة باستخدام API أو مكتبة للشات بوت
//         document.getElementById('chatbox').innerHTML += "<p><strong>بوت:</strong> " + botResponse + "</p>";

//         // السكROLL لأسفل للعرض التلقائي للرسائل الجديدة
//         document.getElementById('chatbox').scrollTop = document.getElementById('chatbox').scrollHeight;
//     }
// }

// // وظيفة لتوليد إجابة بسيطة من الشات بوت
// function generateResponse(userMessage) {
//     // هنا يمكن إضافة أي منطق لإجابة الشات بوت، مثل استخدام قواعد بسيطة أو ربط API
//     if(userMessage.toLowerCase().includes('Hello')) {
//         return "Welcomed! How can I help you today?";
//     } else if(userMessage.toLowerCase().includes('help')) {
//         return "For sure! How can I help you?";
//     } else {
//         return "Sorry, I didn't understand your question. I can help you with anything else";
//     }
// }
