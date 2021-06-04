from Config import outputFile
from Scripts.HTML_Reports.history_data_read import HistoryDataRead


class HTMLReport:

    def __init__(self, path):
        self.outputFilePath = path
        self.file = open(self.outputFilePath, "wt")

        self.__history_data_path = outputFile.OUTPUT_PATH['E2E_output_history']
        self.history_dict = HistoryDataRead(self.__history_data_path)
        self.history_dict.excel_data_dict()

    def html_css(self, environment, sprint, date_time, use_case, result, total, success, fail, fail_color):
        self.file.write("""
        <html>
        <head>
<script type="text/javascript">

var barChartData = {
  labels: [
    "Sprint 1",
    "Sprint 2",
    "Sprint 3",
    "Sprint 4",
    "Sprint 5"
  ],
  datasets: [
    {
      label: "AMSIN",
      backgroundColor: "#9caad6",
      borderColor: "#9caad6",
      borderWidth: 1,
      data: [3, 5, 6, 7,3]
    },
    {
      label: "BETA",
      backgroundColor: "#d88589",
      borderColor: "#d88589",
      borderWidth: 1,
      data: [4, 7, 3, 6, 10]
    },
    {
      label: "AMS",
      backgroundColor: "#98e1d2",
      borderColor: "#98e1d2",
      borderWidth: 1,
      data: [10,7,4,6,9]
    },
    {
     label: "INDIA",
      backgroundColor: "#b9de94",
      borderColor: "#b9de94",
      borderWidth: 1,
      data: [6,9,7,3,10]
    }
  ]
};
var timer_barChartData = {
  labels: [
    "Sprint 1",
    "Sprint 2",
    "Sprint 3",
    "Sprint 4",
    "Sprint 5"
  ],
  datasets: [
    {
      label: "AMSIN",
      backgroundColor: "#9caad6",
      borderColor: "#9caad6",
      borderWidth: 1,
      data: [3, 5, 6, 7,3]
    },
    {
      label: "BETA",
      backgroundColor: "#d88589",
      borderColor: "#d88589",
      borderWidth: 1,
      data: [4, 7, 3, 6, 10]
    },
    {
      label: "AMS",
      backgroundColor: "#98e1d2",
      borderColor: "#98e1d2",
      borderWidth: 1,
      data: [10,7,4,6,9]
    },
    {
     label: "INDIA",
      backgroundColor: "#b9de94",
      borderColor: "#b9de94",
      borderWidth: 1,
      data: [6,9,7,3,10]
    }
  ]
};
var chartOptions = {
  responsive: true,
  legend: {
    position: "bottom"
  },
  title: {
    display: true,
    text: "Last 5 Sprints (Use Cases) Report"
  },
  scales: {
    yAxes: [{
    scaleLabel: {
        display: true,
        labelString: 'Use Cases'
      },
      ticks: {
        beginAtZero: true
      }
    }]
  }
}
var chart_time_Options = {
  responsive: true,
  legend: {
    position: "bottom"
  },
  title: {
    display: true,
    text: "Last 5 Sprints (Time Taken) Report"
  },
  scales: {
    yAxes: [{
    scaleLabel: {
        display: true,
        labelString: 'Time (min)'
      },
      ticks: {
        beginAtZero: true
      }
    }]
  }
}
window.onload = function() {
  var ctx = document.getElementById("canvas").getContext("2d");
  var ctx_time = document.getElementById("canvas_time").getContext("2d");
  window.myBar = new Chart(ctx, {
    type: "bar",
    data: barChartData,
    options: chartOptions
  });
  window.myBar = new Chart(ctx_time, {
    type: "bar",
    data: timer_barChartData,
    options: chart_time_Options
  });
};

</script> 
<style>.marginZero 
    {
        margin: 0;
    }
    .zeroPad {
        padding: 0
    }
    .wid600 {
        max-width: 600px;
    }
    .tablee {
        border: 1px solid #e2e2e2;
        background: "white"
    }
    .fontF {
        font-family: Inter, Segoe UI, Roboto, Arial, verdana, geneva, sans-serif;

    }
    .footer {
        font-size: 11px;
        font-weight: 400;
        line-height: 18px;
        text-align: left;
        color: #a6a6a6
    }
    .collapseBorder {
        border-collapse: collapse;
    }
    .line {
        line-height: 0;

    }
    .summaryHeads {
        padding: 6px 8px;
        font-size: 12px;
        font-weight: 700;
        line-height: 16px;
        text-align: left;
        color: #6b6b6b;
        border-top: 1px solid #ededed;
    }
    .summaryRow {
        padding: 6px 8px;
        font-size: 12px;
        font-weight: 400;
        line-height: 16px;
        text-align: left;
        color: #6b6b6b;
        border-top: 1px solid #ededed;
        border-bottom: 1px solid #ededed;
        width: 124px;
        max-width: 124px
    }
    .emptyCell {
        border-top: 1px solid #ededed;
        width: 124px;
        font-size: 12px;
        line-height: 16px;
        text-align: left;
        max-width: 124px
    }
    .summHeader {
        font-size: 16px;
        font-weight: 700;
        line-height: 20px;
        letter-spacing: -.12px;
        text-align: left
    }
    .graphLabel {
        color: #000;
        font-size: 10px;
        font-weight: 700;
        line-height: 20px;
        text-align: center
    }
    .latestSlot {
        border-radius: 3px;
        max-width: 32px;
        max-height: 80px;
        font-size: 55px;
        line-height: 55px;
        background-color: #d51d11;
        height: 80px
    }
    .prevSlot {
        border-radius: 3px;
        max-width: 32px;
        max-height: 80px;
        font-size: 55px;
        line-height: 55px;
        background-color: #e78b85;
        height: 80px
    }
    .fszero {
        font-size: 0
    }
    .pad48 {
        padding: 48px 48px 0 48px
    }
    .breakWord {
        word-break: break-word
    }
    .alink {
        cursor: pointer;
        color: #0265d2;
        text-decoration: none
    }
    .resultBtn {
        display: inline-block;
        background: #4ec1edf0;
        color: #fff;
        font-size: 12px;
        font-weight: 700;
        line-height: 20px;
        margin: 0;
        text-decoration: none;
        text-transform: none;
        padding: 6px 16px 6px 16px;
        border-radius: 3px
    }

    .table1 {
        border-spacing: 15px;
    }
    .btn {
    /* background: #fff;
    border:3px solid grey;
    padding: 5px;
    width: 200px; */
    text-align:left;
}
#btn_container img {
    /* border: 6px solid red;
    margin-right: 5px;     */
    vertical-align: middle;
}
.btn-txt {
    padding-left: 5px;
    vertical-align: middle;
}
.Pass{
    color: green;
    font-size: 17px !important;
    font-weight: bold !important;
}
.Fail{
    color: red;
    font-size: 17px !important;
    font-weight: bold !important;
}
.summaryPass{
color: green;
font-weight: bold !important;
}
.summaryFail{
color: red;
font-weight: bold !important;
}
.canvasjs-chart-credit
{
    display: none !important;
}
</style>
</head>
<body>

<div class="marginZero zeroPad fontF">
    <center>
        <div class="wid600 marginZero tablee">
            <table class="wid600  collapseBorder">
                <tbody>
                    <tr>
                        <td class="tdclass line fszero collapseBorder">
                            <table class="collapseBorder">
                                <tbody>
                                    <tr>
                                        <td class="fontF collapseBorder pad48">
                                            <table class="collapseBorder">
                                                <tbody>
                                                    <tr>
                                                        <td align="left" class="fontF collapseBorder fszero breakWord">
                                                            <a href="">
                                                                <img width="142"
                                                                    src="https://hirepro.in/wp-content/uploads/2020/08/hirepro-new-logo-dark-slim.png"
                                                                    style="border:0;display:block;outline:0;text-decoration:none;height:auto">
                                                            </a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="fontF collapseBorder" style="padding-top:32px">
                                                            <div class="breakWord fontF"
                                                                style="font-size:20px;font-weight:700;line-height:24px;text-align:left;letter-spacing:-.56px">
                                                                Automated Test Reporting - """ + str(date_time) + """</div>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding-top:32px">
                                                            <table border="0" cellpadding="0" cellspacing="0"
                                                                width="498"
                                                                style="border-collapse:collapse;width:498px">
                                                                <tbody>
                                                                    <tr>
                                                                        <td style="border-collapse:collapse;border-top:1px solid #ededed;font-size:0;text-align:center;width:498px"
                                                                            width="498">
                                                                            <div style="font-size:0;text-align:left;display:inline-block;vertical-align:middle;width:498px!important"
                                                                                width="498">
                                                                                <table border="0" cellpadding="0"
                                                                                    cellspacing="0" width="498"
                                                                                    style="border-collapse:collapse;width:498px">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:600;line-height:16px;text-align:left;color:#6b6b6b">
                                                                                                    Monitor</div>
                                                                                            </td>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="word-break:break-all;word-wrap:break-word;overflow:hidden;font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:400;line-height:16px;text-align:left;color:#000">
                                                                                                    <a
                                                                                                        class="alink">Vinod Eraganaboina</a>
                                                                                                </div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td style="border-collapse:collapse;border-top:1px solid #ededed;font-size:0;padding:0;text-align:center;width:498px"
                                                                            width="498">
                                                                            <div style="font-size:0;text-align:left;display:inline-block;vertical-align:middle;width:498px!important"
                                                                                width="498">
                                                                                <table border="0" cellpadding="0"
                                                                                    cellspacing="0" width="498"
                                                                                    style="border-collapse:collapse;width:498px">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px;"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:600;line-height:16px;text-align:left;color:#6b6b6b">
                                                                                                    Collection</div>
                                                                                            </td>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="word-break:break-all;word-wrap:break-word;overflow:hidden;font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:400;line-height:16px;text-align:left;color:#000">
                                                                                                    <a
                                                                                                        class="alink">""" + use_case + """</a>
                                                                                                </div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td style="border-collapse:collapse;border-top:1px solid #ededed;font-size:0;padding:0;text-align:center;width:498px"
                                                                            width="498">
                                                                            <div style="font-size:0;text-align:left;display:inline-block;vertical-align:middle;width:498px!important"
                                                                                width="498">
                                                                                <table border="0" cellpadding="0"
                                                                                    cellspacing="0" width="498"
                                                                                    style="border-collapse:collapse;width:498px">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:600;line-height:16px;text-align:left;color:#6b6b6b">
                                                                                                    Environment</div>
                                                                                            </td>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="word-break:break-all;word-wrap:break-word;overflow:hidden;font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:400;line-height:16px;text-align:left;color:#000">
                                                                                                    <a
                                                                                                        class="alink">""" + environment + """</a>
                                                                                                </div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td style="border-collapse:collapse;border-top:1px solid #ededed;font-size:0;padding:0;text-align:center;width:498px"
                                                                            width="498">
                                                                            <div style="font-size:0;text-align:left;display:inline-block;vertical-align:middle;width:498px!important"
                                                                                width="498">
                                                                                <table border="0" cellpadding="0"
                                                                                    cellspacing="0" width="498"
                                                                                    style="border-collapse:collapse;width:498px">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:600;line-height:16px;text-align:left;color:#6b6b6b">
                                                                                                    Workspace</div>
                                                                                            </td>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="word-break:break-all;word-wrap:break-word;overflow:hidden;font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:400;line-height:16px;text-align:left;color:#000">
                                                                                                    <a class="alink">UI Automation</a>
                                                                                                </div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td style="border-collapse:collapse;border-top:1px solid #ededed;border-bottom:1px solid #ededed;font-size:0;padding:0;text-align:center;width:498px"
                                                                            width="498">
                                                                            <div style="font-size:0;text-align:left;display:inline-block;vertical-align:middle;width:498px!important"
                                                                                width="498">
                                                                                <table border="0" cellpadding="0"
                                                                                    cellspacing="0" width="498"
                                                                                    style="border-collapse:collapse;width:498px">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:600;line-height:16px;text-align:left;color:#6b6b6b">
                                                                                                    Sprint</div>
                                                                                            </td>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="font-family:Inter,Segoe UI,Roboto,Arial,verdana,geneva,sans-serif;font-size:12px;font-style:normal;font-weight:400;line-height:16px;text-align:left;color:#000">
                                                                                                   
                                                                                                     <a class="alink"> """ + sprint + """</a>
                                                                                                     </div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td style="border-collapse:collapse;border-top:1px solid #ededed;border-bottom:1px solid #ededed;font-size:0;padding:0;text-align:center;width:498px"
                                                                            width="498">
                                                                            <div style="font-size:0;text-align:left;display:inline-block;vertical-align:middle;width:498px!important"
                                                                                width="498">
                                                                                <table border="0" cellpadding="0"
                                                                                    cellspacing="0" width="498"
                                                                                    style="border-collapse:collapse;width:498px">
                                                                                    <tbody>
                                                                                        <tr>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div
                                                                                                    style="font-size:12px;font-style:normal;font-weight:600;line-height:16px;text-align:left;color:#6b6b6b">
                                                                                                    Result</div>
                                                                                            </td>
                                                                                            <td align="left"
                                                                                                style="border-collapse:collapse;font-size:0;padding:6px 8px;word-break:break-word;vertical-align:middle;width:249px"
                                                                                                valign="middle"
                                                                                                width="249">
                                                                                                <div style="font-size:12px;font-style:normal;line-height:16px;text-align:left" class=""" + result + """>
                                                                                                """ + result + """
                                                                                                </div>
                                                                                            </td>
                                                                                        </tr>
                                                                                    </tbody>
                                                                                </table>
                                                                            </div>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div   style="text-align:left;display:inline-block;width:100%">
            <table style="border-collapse:collapse;margin: 0 auto;">
                <tbody>
                    <tr>
                        <td style="padding:0">
                            <table style="border-collapse:collapse">
                                <tbody>
                                    <tr>
                                        <td align="left"
                                            style="    padding: 0 0 24px 0;;word-break:break-word">
                                            <table class="table1"
                                                style="border-collapse:separate;line-height:100%">
                                                <tbody>
                                                    <tr>
                                                        <td
                                                            style="border:none;border-radius:3px;background:#4ec1edf0">
                                                            <!-- <a href=""
                                                                class="resultBtn">View
                                                                Run
                                                                Results<img src="https://img-premium.flaticon.com/png/512/3409/3409512.png?token=exp=1622635273~hmac=8d80e46107434537e9c17ba7fe1fb6e8"></a> -->
                                                                <a href="" title="HTML Web Report" class="btn resultBtn" style=" border:none;padding-left: 10px;">               
                                                                    <div id="btn_container"><img  src="https://image.flaticon.com/icons/png/512/4599/4599587.png" width="25" height="25"/><span class="btn-txt">View
                                                                Run
                                                                Results</span></div>
                                                                </a>
                                                            </td>
                                                        <td
                                                            style="border:none;border-radius:3px;background:#4ec1edf0">
                                                            <!-- <a href=""
                                                                class="resultBtn">Excel
                                                                Download</a> -->
                                                                <a href="" title="Download Excel Report" class="btn resultBtn" style=" border:none;padding-left: 10px;">
                                                                    <div id="btn_container"><img  src="https://image.flaticon.com/icons/png/512/3325/3325366.png" width="25" height="25"/><span class="btn-txt">Excel
                                                                        Download</span></div>
                                                                </a>
                                                        </td>&nbsp;
                                                        <td
                                                            style="border:none;border-radius:3px;background:#4ec1edf0">
                                                            <!-- <a href=""
                                                                class="resultBtn">Google Drive</a> -->
                                                                <a title="sprint wise automation reports" href="https://drive.google.com/drive/u/1/folders/186nL7DWI_ZoMklgcwIUykC4tSQuECtGH" target="_blank"  class="btn resultBtn" style=" border:none;padding-left: 10px;">
                                                                    <div id="btn_container"><img  src="https://image.flaticon.com/icons/png/512/2111/2111436.png" width="25" height="25"/><span class="btn-txt">Google
                                                                        Drive</span></div>
                                                                </a>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>

                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
            <div style="padding:32px 48px 32px 40px;max-width:598px">
                <div id="container" style="margin-top:2rem;height: 300px; width: 100%;">
                  <canvas id="canvas_time"></canvas>
                  <div style="font-size:12px;font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    font-weight: 600;"> <p> Chart legends are clickable to view the specific items </p> </div>
                </div>
            </div>
            <div style="padding:0 48px 48px 48px">
               <div id="container" style="margin-top:2rem;height: 300px; width: 100%;">
                  <canvas id="canvas"></canvas>
                  <div style="font-size:12px;font-family: 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    font-weight: 600;"> <p> Chart legends are clickable to view the specific items </p> </div>
                </div>
                <table style="border-collapse:collapse">
                    <tbody>
                        <tr>
                            <td style="padding-top:32px;text-align:left;">
                                <div class="summHeader">Last run summary</div>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding-top:16px">
                                <table>
                                    <tbody>
                                        <tr>
                                            <td class="emptyCell">
                                                &nbsp;</td>
                                            <td class="summaryHeads"> Passed</td>
                                            <td class="summaryHeads">Failed</td>
                                            <td class="summaryHeads">Total</td>
                                        </tr>
                                        <tr>
                                            <td class="summaryHeads" style="border-bottom:1px solid #ededed;">Tests</td>
                                            <td class="summaryRow summaryPass">""" + str(success) + """</td>
                                            <td class="summaryRow """ + fail_color + """ ">""" + str(fail) + """</td>
                                            <td class="summaryRow" style="font-weight:bold;color: black;">""" + str(
            total) + """</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding:2rem 0 15px 0;">
                                <p style="border-top:solid 2px #ededed;font-size:1px;margin:0 auto;width:100%">
                                </p>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="footer">
                                    © 2021 HirePro . All rightsreserved.<br>
                                    Plot No. 53, Kariyammana Agrahara Road,Devarabisana Halli, Bengaluru – 560 103
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </center>
</div>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.bundle.js"></script>
</body>
</html>
        """)