import smtplib
import datetime
from email.message import EmailMessage
from email.mime.text import MIMEText

class HtmlReporter(object):
    def __init__(self, evaluation_data):
        self._data = evaluation_data
        self._head = '''
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title></title>
            <style media="screen">
              body {
                background-color: LightYellow;
                width: 900px;
              }
              header {
                text-align: center;
              }
              div {
                text-align: center;
              }
              section {
                height: 50px;
                text-align: center;
              }
              article {
                font-size: 12px;
                text-align: center;
                color: blue;
                width: 900px;
                margin-left: auto;
                margin-right: auto;
              }
              figure {
                background-color: Cornsilk;
                width: 900px;
                margin-left: auto;
                margin-right: auto;
              }
              footer {
                text-align: center;
                padding: 3px;
                background-color: white;
                color: blue;
              }
              table {
                width: 900px;
                text-align:right;
                border-collapse: collapse;
                margin-left: auto;
                margin-right: auto;
              }
              th {
                background-color: Brown;
                color: white;
              }
              .img {
                width: 900px;
              }
              .low {
                background-color: lightgreen;
              }
              .mid {
                background-color: PapayaWhip;
              }
              .high {
                background-color: tomato;
              }
            </style>
          </head>
          <body>
        '''
        self._tail = '''
            <footer>
              <p> 以上信息仅供参考。 </p>
            </footer>
          </body>
        </html>
        '''

    def construct_valuation_table(self):
        etf_table = """
        <header>
            <h3>指数估值表</h3>
        </header>
        <div>
            <table>
              <tr>
                <th>指数代码</th>
                <th>指数名称</th>
                <th>市盈率</th>
                <th>市盈率百分位</th>
                <th>市净率</th>
                <th>市净率百分位</th>
                <th>股息</th>
                <th>ROE</th>
                <th>估值状态</th>
                <th>日期</th>
              </tr>
        """

        for i in range(len(self._data)):
            index_code = self._data.loc[i, 'index_code']
            name = self._data.loc[i, 'name']
            pe = self._data.loc[i, 'pe']
            pe_percentile = self._data.loc[i, 'pe_percentile']
            pb = self._data.loc[i, 'pb']
            pb_percentile = self._data.loc[i, 'pb_percentile']
            yeild = self._data.loc[i, 'yeild']
            roe = self._data.loc[i, 'roe']
            eva_type = self._data.loc[i, 'eva_type']
            date = self._data.loc[i, 'date']

            etf_table += """
            <tr  class="{}">
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
            """.format(eva_type,
                       index_code,
                       name,
                       str(round(pe, 2)),
                       str(round(pe_percentile * 100, 2)) + '%',
                       str(round(pb, 2)),
                       str(round(pb_percentile * 100, 2)) + '%',
                       str(round(yeild, 2)),
                       str(round(roe * 100, 2)) + '%',
                       date)

        etf_table += """
        </table>
        </div>
        <section> </section>
        """

        return etf_table

    def send_email(self):
        msg = EmailMessage()

        # 填充邮件头部
        msg['Subject'] = '指数估值 - ' + str(datetime.date.today())
        msg['From'] = 'lianbch@163.com'
        msg['To'] = 'lianbch@163.com'

        # 填充邮件正文
        html = self._head \
               + self.construct_valuation_table() \
               + self._tail
        msg.add_attachment(html, subtype='html')

        # 发送邮件
        try:
            mail_server = smtplib.SMTP_SSL('smtp.163.com',port=465)
            mail_server.login(sender, 'FVVFEMTFLXCRLQXS')
            mail_server.send_message(msg)
        except smtplib.SMTPException as ex:
            print("Error: send failure = ", ex)
