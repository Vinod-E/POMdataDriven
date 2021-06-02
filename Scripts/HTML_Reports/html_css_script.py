class HTMLReport:

    def __init__(self, path):
        self.outputFilePath = path
        self.file = open(self.outputFilePath, "wt")

    def html_css(self, environment, sprint, date_time, use_case, result, total, success, fail):
        self.file.write("""<style>
    .marginZero {
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
    animation: blur .99s ease-out infinite;
    text-shadow: 0px 0px 5px green, 0px 0px 7px #fff;
    font-size: 17px !important;
    font-weight: bold !important;
}
.Fail{
    color: red;
    animation: blur .99s ease-out infinite;
    text-shadow: 0px 0px 5px red, 0px 0px 7px #fff;
    font-size: 17px !important;
    font-weight: bold !important;
}
@keyframes blur {
  from {
    text-shadow:0px 0px 10px #fff,
      0px 0px 1px #fff, 
      0px 0px 5px #fff,
      0px 0px 10px #fff,
      0px 0px 15px #fff,
      0px 0px 20px #fff,
      0px 0px 25px #fff,
      0px 0px 25px #fff,
      0px 0px 50px #fff,
      0px 0px 50px #7B96B8,
      0px 10px 100px #7B96B8,
      0px -10px 100px #7B96B8,
      0px -10px 100px #7B96B8;
  }
}
</style>
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
                                                                Automated Test Reporting - """+str(date_time)+"""</div>
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
                                                                                                        class="alink">"""+use_case+"""</a>
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
                                                                                                        class="alink">"""+environment+"""</a>
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
                                                                                                   
                                                                                                     <a class="alink"> """+sprint+"""</a>
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
                                                                                                <div style="font-size:12px;font-style:normal;line-height:16px;text-align:left" class="""+result+""">
                                                                                                """+result+"""
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
            <div style="background:#F9F9F9;padding:32px 48px 32px 40px;max-width:598px">
                <table style="border-collapse:collapse">
                    <tbody>
                        <tr valign="top">
                            <td align="left"
                                style="padding-left:8px;line-height:20px;font-size:16px;max-width:480px;min-height:16px">
                                <div
                                    style="font-size:16px;font-weight:700;letter-spacing:-.12px;text-align:left;color:#000">
                                    Last 10 runs</div>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding-top:16px;max-width:480px;width:480px" width="480">
                                <table align="left" width="480" style="width:480px;max-width:480px">
                                    <tbody>
                                        <tr valign="top">
                                            <td width="48" style="width:48px;min-width:48px;word-break:break-word">
                                                <table width="32" style="width:32px;max-width:32px;min-width:32px">
                                                    <tbody>
                                                        <tr>
                                                            <td width="32px" style="border-collapse:collapse">
                                                                <div class="prevSlot">&hairsp;</div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <div style="padding-top:2px;text-align:left;width:100%">
                                                    <table class="collapseBorder">
                                                        <tbody>
                                                            <tr>
                                                                <td class="graphLabel">10:&zwnj;37 </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel">AM </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel">Jun </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel">1 </td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </td>
                                            <td width="48" style="width:48px;min-width:48px;word-break:break-word">
                                                <table width="32" style="width:32px;max-width:32px;min-width:32px">
                                                    <tbody>
                                                        <tr>
                                                            <td>
                                                                <div class="prevSlot">&hairsp;</div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <div style="padding-top:2px;text-align:left;width:100%">
                                                    <table class="collapseBorder">
                                                        <tbody>
                                                            <tr>
                                                                <td class="graphLabel">
                                                                    10:&zwnj;37 </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel">
                                                                    AM </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel"></td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel"></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </td>
                                            <td style="width:48px;min-width:48px;word-break:break-word">
                                                <table style="width:32px;max-width:32px;min-width:32px">
                                                    <tbody>
                                                        <tr>
                                                            <td class="collapseBorder">
                                                                <div class="latestSlot">&hairsp;</div>
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                                <div style="padding-top:2px;text-align:left;width:100%">
                                                    <table class="collapseBorder">
                                                        <tbody>
                                                            <tr>
                                                                <td class="graphLabel">10:&zwnj;40 </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel">AM </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel"></td>
                                                            </tr>
                                                            <tr>
                                                                <td class="graphLabel"></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>
                                                </div>
                                            </td>
                                            <td style="font-size:1px;line-height:1px">&nbsp;</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div style="padding:0 48px 48px 48px">
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
                                            <td class="summaryRow">"""+str(success)+"""</td>
                                            <td class="summaryRow">"""+str(fail)+"""</td>
                                            <td class="summaryRow">"""+str(total)+"""</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="padding:18px 0 15px 0;">
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
        """)
