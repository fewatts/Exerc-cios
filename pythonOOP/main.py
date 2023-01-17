from op import Conta
import op

conta = op.Conta('34583-9', 'wednesday', 120, 10000)
conta.deposita(20.0)
conta.extrato()
