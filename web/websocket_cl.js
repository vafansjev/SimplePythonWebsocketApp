document.addEventListener('DOMContentLoaded', function (){

    const messagesContainer = document.querySelector("#messages_container");
    const messageInput = document.querySelector('[name=message_input]')
    const sendMessageButton = document.querySelector('[name=send_message_button]')
    const connectionButton = document.querySelector('[name=connect_button]')



    connectionButton.onclick = () => {
        const serverUrl = document.querySelector('[name=server_text]').value
        const websocketClient = new WebSocket(serverUrl);


        websocketClient.onopen = () => {
            sendMessageButton.onclick = () => {
                websocketClient.send(messageInput.value);
                messageInput.value="";
            };


        websocketClient.onmessage = (message) => {
            const newMessage = document.createElement('div');
            newMessage.innerHTML = message.data;
            messagesContainer.appendChild(newMessage)

            };

        };

    };


}, false)