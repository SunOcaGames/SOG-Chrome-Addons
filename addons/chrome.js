// ==UserScript==
// @name         SOG-Chrome-Addons
// @namespace    http://tampermonkey.net/
// @version      0.63
// @description  太陽之海遊戲工作室的瀏覽器外掛公用程式
// @author       Dong
// @match        https://scratch.mit.edu/*
// @icon         https://sunocagames.github.io/SunOcaGames/img/sun_logo_%E6%AD%A3%E6%96%B9%E5%BD%A2.png
// @grant        none
// ==/UserScript==

(function() {
    setInterval(() => {
      if ('https://scratch.mit.edu/'==location.href) {
        var namespan=document.getElementsByClassName('profile-name')
        console.log(namespan[0].innerText)
      } else if ('https://scratch.mit.edu/projects/'.indexOf(location.href)!=-1) {
        namespan=document.getElementsByClassName('user-name')
        console.log(namespan[0].innerText)
      }
    }, 1000);
})();