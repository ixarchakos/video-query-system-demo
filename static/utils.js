//enable/disable table rows
function modal_checkbox_display(car, truck, person) {
  if (truck && person && car) {
    document.getElementById('row1').style.display = '';
    document.getElementById('row2').style.display = '';
    document.getElementById('row3').style.display = '';
    document.getElementById('row4').style.display = '';
    document.getElementById('row5').style.display = '';
    document.getElementById('row6').style.display = '';
    document.getElementById('row_val1').style.display = '';
    document.getElementById('row_val2').style.display = '';
    document.getElementById('row_val3').style.display = '';
    document.getElementById('row_val4').style.display = '';
    document.getElementById('row_val5').style.display = '';
    document.getElementById('row_val6').style.display = '';
  } else if (car && person) {
    document.getElementById('row1').style.display = '';
    document.getElementById('row2').style.display = '';
    document.getElementById('row_val1').style.display = '';
    document.getElementById('row_val2').style.display = '';
    document.getElementById('row3').style.display = 'none';
    document.getElementById('row4').style.display = 'none';
    document.getElementById('row5').style.display = 'none';
    document.getElementById('row6').style.display = 'none';
    document.getElementById('row_val3').style.display = 'none';
    document.getElementById('row_val4').style.display = 'none';
    document.getElementById('row_val5').style.display = 'none';
    document.getElementById('row_val6').style.display = 'none';
  } else if (truck && person) {
    document.getElementById('row1').style.display = '';
    document.getElementById('row2').style.display = '';
    document.getElementById('row_val1').style.display = '';
    document.getElementById('row_val2').style.display = '';
    document.getElementById('row3').style.display = 'none';
    document.getElementById('row4').style.display = 'none';
    document.getElementById('row5').style.display = 'none';
    document.getElementById('row6').style.display = 'none';
    document.getElementById('row_val3').style.display = 'none';
    document.getElementById('row_val4').style.display = 'none';
    document.getElementById('row_val5').style.display = 'none';
    document.getElementById('row_val6').style.display = 'none';
  } else if (car && truck ) {
    document.getElementById('row1').style.display = '';
    document.getElementById('row2').style.display = '';
    document.getElementById('row_val1').style.display = '';
    document.getElementById('row_val2').style.display = '';
      document.getElementById('row3').style.display = 'none';
    document.getElementById('row4').style.display = 'none';
    document.getElementById('row5').style.display = 'none';
    document.getElementById('row6').style.display = 'none';
    document.getElementById('row_val3').style.display = 'none';
    document.getElementById('row_val4').style.display = 'none';
    document.getElementById('row_val5').style.display = 'none';
    document.getElementById('row_val6').style.display = 'none';
  } else {
    document.getElementById('row1').style.display = 'none';
    document.getElementById('row2').style.display = 'none';
    document.getElementById('row3').style.display = 'none';
    document.getElementById('row4').style.display = 'none';
    document.getElementById('row5').style.display = 'none';
    document.getElementById('row6').style.display = 'none';
    document.getElementById('row_val1').style.display = 'none';
    document.getElementById('row_val2').style.display = 'none';
    document.getElementById('row_val3').style.display = 'none';
    document.getElementById('row_val4').style.display = 'none';
    document.getElementById('row_val5').style.display = 'none';
    document.getElementById('row_val6').style.display = 'none';
  }
};

//refresh frane
function refresh(flag, ii, refreshInterval, inputVideo, results_id){
    img.src = url + "?t=" + new Date().getTime();
    setTimeout("init(" + flag + " , " + ii + " , " + refreshInterval + " , '" + inputVideo + "' , '" + results_id + "' )",refreshInterval);
}