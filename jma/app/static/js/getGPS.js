// Geolocation APIに対応している
if (navigator.geolocation) {
    document.getElementById("alert").innerHTML = "この端末は利用可能です";
  } else {
    document.getElementById("alert").innerHTML = "位置情報を有効にしてください";
    //document.getElementById("go").disabled = true;
  }

  // 現在地取得処理
  function getPosition() {
    // 現在地を取得
    navigator.geolocation.getCurrentPosition(
      // 取得成功した場合
      function(position) {
            document.getElementById("lon").value = position.coords.longitude;
            document.getElementById("lat").value = position.coords.latitude;
            //document.getElementById("lon").value = 139.8267;
            //document.getElementById("lat").value = 38.7272;
            //35.4682° N, 133.0484° E
            console.log(position.coords.longitude);
            console.log(position.coords.latitude);
      },
      function(error) {
        const button = document.getElementById("go");
        button.disabled = true;
        switch(error.code) {
          case 1: //PERMISSION_DENIED
            document.getElementById("alert").innerHTML = "位置情報が許可されていないため、利用できません。";
            break;
          case 2: //POSITION_UNAVAILABLE
            document.getElementById("alert").innerHTML = "位置情報が取得できませんでした。";
            break;
          case 3: //TIMEOUT
            document.getElementById("alert").innerHTML = "タイムアウトになりました。";
            break;
          default:
            document.getElementById("alert").innerHTML = "その他のエラー(エラーコード:"+error.code+")";
            break;
        }
      }
    );
    
  }