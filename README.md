# NexoGest - bot de atendimento (versão terminal)

Bot de atendimento em Python para a NexoGest (Tiago Tessarolo Lda), ligado à base de dados em SQLite.
Reconhece pelo número de telemóvel se quem escreve é cliente ou administrador.

## Como correr

Na pasta `projeto`:

```
python inicio.py
```

Precisa do `pandas` (`pip install pandas`).
Números de teste: cliente `912000000` · administrador `912345679`

## Organização

```
projeto/
├── inicio.py        pede o número e abre o menu certo
├── admin/           menu do administrador
├── cliente/         menu do cliente
├── base_dados/      nexogest.db, ligação e scripts da base
└── documentos/      guiões da apresentação
```
