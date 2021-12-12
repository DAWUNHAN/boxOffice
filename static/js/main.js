window.addEventListener('load', function() { 
    let message = { height: document.body.scrollHeight, width: document.body.scrollWidth }; 
    window.top.postMessage(message, "*"); 
});





