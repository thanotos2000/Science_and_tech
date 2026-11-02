const { session, webContents, net } = require("electron");
const webviewSession = session.fromPartition("persist:mx-player-0cd059f4c4c262ea");
const webContent = webContents.fromId({});
webviewSession.webRequest.onSendHeaders(
  { 
    urls: ["https://api.bilibili.com/x/player/v2*","https://api.bilibili.com/x/player/wbi/v2*"], type: ["xhr"]
  }, ({url, method, requestHeaders, webContentsId}) => {
    if (method !== "GET" || webContentsId===undefined) return;
    webContent.send("mx:http_proxy", {type:"player_v2" ,url, method, requestHeaders, webContentsId});
  })