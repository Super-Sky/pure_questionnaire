import xlwt
import json


#回答数据导出excel
def analysisExportExcel(data,title='问卷统计'):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('数据统计')
    for index,question in enumerate(data):
        for i in range(len(question)):
            ws.write(index,i,question[i])
    return wb


def answerText2Excel(data):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('回答详情')
    i=0
    j=0
    # print('data=',data)
    for item in data:
        ws.write(i,j,item)
        i+=1
    return wb



if __name__=="__main__":
    pass
    # data=json.loads(data)
    # analysisExportExcel(data['detail'])

