购买突发性能实例后，如果您打开无性能约束模式并且使用了超额CPU积分，还需要支付额外费用。本文介绍如何查看突发性能实例账单。  

## 操作步骤
1. 访问[费用与成本中心-账单详情](https://billing-cost.console.aliyun.com/finance/expense-report/expense-detail-by-instance)。

2. 查询突发性能实例账单。

   1. 在**账单详情**页面，设置如下参数，然后单击**搜索**。

      未提及的参数请保持默认。
      <table> <thead> <tr> <td> <p><b>参数</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>统计项</b></p> </td> <td> <p>选择<b>计费项</b>。</p> </td> </tr> <tr> <td> <p><b>账单月份</b></p> </td> <td> <p>选择需要查看的账单月份。</p> </td> </tr> <tr> <td> <p><b>产品名称</b></p> </td> <td> <p>选择<b>云服务器ECS</b>。</p> </td> </tr> <tr> <td> <p><b>资源实例名称/ID</b></p> </td> <td> <p>输入需要查询的突发性能实例名称或ID。</p> </td> </tr> </tbody> </table>
   2. 页面下方即可展示已查询的突发性能实例账单，计费项为**超额积分**即为使用超额积分产生的账单。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0405463471/p936884.png)

      <br />

3. 查询CPU积分使用明细。

   1. 单击页面右上角的**查看用量明细**。

   2. 设置如下参数，然后单击**导出CSV**。

      <table> <thead> <tr> <td> <p><b>参数</b></p> </td> <td> <p><b>说明</b></p> </td> </tr> </thead> <colgroup></colgroup> <colgroup></colgroup> <tbody> <tr> <td> <p><b>时间周期</b></p> </td> <td> <p>根据需要，选择需要查看的时间。</p> </td> </tr> <tr> <td> <p><b>商品名称</b></p> </td> <td> <p>选择<b>云服务器 ECS-按量付费</b>或<b>云服务器 ECS-包年包月</b>。</p> </td> </tr> <tr> <td> <p><b>计费项名称</b></p> </td> <td> <p>选择<b>超额积分</b>。</p> </td> </tr> <tr> <td> <p><b>计量规格</b></p> </td> <td> <p>选择<b>CPU积分</b>。</p> </td> </tr> <tr> <td> <p><b>计量粒度</b></p> </td> <td> <p>当前仅支持选择<b>原始</b>。</p> </td> </tr> </tbody> </table>
   3. 打开CSV表格，即可查看超额CPU积分用量明细，**cpu性能积分**列即为使用的超额积分。

      ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0405463471/p936893.png)
