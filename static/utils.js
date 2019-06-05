//enable/disable table rows
function modal_checkbox_display(car, truck, person, bus) {
  if (truck && person && car && bus) {
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
  } else if (car && bus) {
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
function refresh(flag, ii, refreshInterval, inputVideo, results_id, predicates, bbox){
    
    var bbox_array = [];
    if (typeof bbox !== 'undefined'){
    bbox.forEach(function (item, key, mapObj){
      bbox_array.push(item);
    });
    }
    img.src = url + "?t=" + new Date().getTime();
    setTimeout("init(" + flag + " , " + ii + " , " + refreshInterval + " , '" + inputVideo + "' , '" + results_id + "' , '" + predicates + "' , '" + bbox_array + "' )",refreshInterval);
}

// change the visibility of predicate selection on advanced queries
function predicates_button_visibility(inputVideo){
    var algorithm = $('input[name="project1"]:checked').val();
    var count_query = "SELECT cameraID, count(frameID), C1(F1(vehBox1)) AS vehType1, C3(F3(SignBox1)) AS SignType2, C2(F2(vehBox1)) AS vehColor FROM (PROCESS " + inputVideo + " PRODUCE cameraID, frameID, vehBox1 USING VehDetector, SignBox1 USING SignDetector) WINDOW HOPING (SIZE 5000, ADVANCE BY 5000)";
    if (algorithm == "Count") {
      $('#sql_text').val(count_query);
      $("#predicates_button").css("visibility", "hidden");
    } else {
      $("#predicates_button").css("visibility", "visible");
    }
}


function change_class_visibility_modal(val){
    $("#isCar").prop('disabled', false);
    $("#isTruck").prop('disabled', false);
    $("#isBus").prop('disabled', false);
    $("#isPerson").prop('disabled', false);

  if (val == "detrac"){
        $("#isPerson").prop('disabled', true);
  } else if (val == 'aquarium'){
        $("#isCar").prop('disabled', true);
        $("#isTruck").prop('disabled', true);
        $("#isBus").prop('disabled', true);
  } else if (val == "square") {
        $("#isPerson").prop('disabled', true);
  }
}

function queries_per_filter_predicates(val, inputVideo, map){
    if (val == "count"){
        query = "SELECT cameraID, count(frameID), C1(F1(vehBox1)) AS vehType1, C3(F3(SignBox1)) AS SignType2, C2(F2(vehBox1)) AS vehColor FROM (PROCESS " + inputVideo + " PRODUCE cameraID, frameID, vehBox1 USING VehDetector, SignBox1 USING SignDetector) WINDOW HOPING (SIZE 5000, ADVANCE BY 5000)";
    } else if (val == 'localisation' && map != 0){
        map.forEach(function (item, key, mapObj){
          query = "SELECT cameraID, frameID, C1(F1(vehBox1)) AS vehType1, C3(F3(SignBox1)) AS SignType2, C2(F2(vehBox1)) AS vehColor FROM (PROCESS " + inputVideo + " PRODUCE cameraID, frameID, vehBox1 USING VehDetector, SignBox1 USING SignDetector) WHERE "+ key +" WINDOW HOPING (SIZE 5000, ADVANCE BY 5000)";
        }); 
    } else if (val == 'class count' && map != 0){
        map.forEach(function (item, key, mapObj){
          query = "SELECT cameraID, frameID, C1(F1(vehBox1)) AS vehType1, C3(F3(SignBox1)) AS SignType2, C2(F2(vehBox1)) AS vehColor FROM (PROCESS " + inputVideo + " PRODUCE cameraID, frameID, vehBox1 USING VehDetector, SignBox1 USING SignDetector) WHERE "+ key +" WINDOW HOPING (SIZE 5000, ADVANCE BY 5000)";
        }); 
    }
    return query;
}