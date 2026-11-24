import sys
import random
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import Qt, QTimer
import pyqtgraph as pg

app = QApplication(sys.argv)

janela = QWidget()
janela.setStyleSheet("background-color: black;")
janela.resize(1000, 800)
layout = QVBoxLayout(janela)

def criar_quadrado(titulo, valor_inicial):
    quadrado = QFrame()
    quadrado.setStyleSheet("border: 2px solid #555555; border-radius: 12px;")
    caixa = QVBoxLayout(quadrado)

    label_titulo = QLabel(titulo)
    label_titulo.setAlignment(Qt.AlignCenter)
    label_titulo.setStyleSheet("font-size: 20px; color: #aaaaaa; border: none;")

    label_valor = QLabel(valor_inicial)
    label_valor.setAlignment(Qt.AlignCenter)
    label_valor.setStyleSheet("font-size: 60px; font-weight: bold; color: white; border: none;")

    caixa.addWidget(label_titulo)
    caixa.addWidget(label_valor)
    return quadrado, label_valor

quadrado_vel, texto_vel = criar_quadrado("VELOCIDADE", "-- km/h")
quadrado_temp, texto_temp = criar_quadrado("TEMPERATURA", "-- ºC")

topo = QHBoxLayout()
topo.addWidget(quadrado_vel)
topo.addWidget(quadrado_temp)
layout.addLayout(topo)

grafico = pg.PlotWidget(title="Velocidade")
grafico.setBackground("k")
curva = grafico.plot(pen="y")
layout.addWidget(grafico)

historico = []

def atualizar():
    velocidade = random.uniform(0, 100)
    temperatura = random.uniform(40, 90)

    texto_vel.setText(f"{velocidade:.1f} km/h")
    texto_temp.setText(f"{temperatura:.1f} ºC")

    historico.append(velocidade)
    if len(historico) > 100:
        historico.pop(0)
    curva.setData(historico)

    if temperatura > 65:
        cor = "red"
    else:
        cor = "green"
    texto_temp.setStyleSheet(f"font-size: 60px; font-weight: bold; color: {cor}; border: none;")

timer = QTimer()
timer.timeout.connect(atualizar)
timer.start(500)

janela.show()
sys.exit(app.exec())


#ver como são os dashboards na f1
