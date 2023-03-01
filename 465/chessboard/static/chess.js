function Move(e) {
  if((e && e.keyCode == 13) || e == 0){
    let src = document.getElementById("src").value.toLowerCase();
    let dst = document.getElementById("dst").value.toLowerCase();
    let piece = document.getElementById(src).innerHTML;
    document.getElementById(dst).innerHTML = piece;
    document.getElementById(src).innerHTML = "&nbsp";
  }
}
