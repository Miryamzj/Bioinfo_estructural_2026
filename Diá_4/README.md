# Predicción estructural del dímero MAX unido a ADN (E-box) mediante AlphaFold3

## Descripción

En este proyecto se modeló la interacción proteína-ADN del factor de transcripción humano **MAX (Myc-associated factor X)** utilizando AlphaFold3.\
El objetivo fue reconstruir el complejo biológico formado por un homodímero MAX unido a su motivo de reconocimiento canónico tipo **E-box (5'-CACGTG-3')**.

------------------------------------------------------------------------

## Fundamento biológico

MAX pertenece a la familia de factores de transcripción **bHLH-LZ (basic helix-loop-helix leucine zipper)**.

Estas proteínas:

-   Forman dímeros
-   Reconocen secuencias E-box en el ADN
-   Alcanzan su conformación funcional al unirse al ADN

Por lo tanto, el sistema funcional a modelar es el complejo proteína-ADN completo.

------------------------------------------------------------------------

## Metodología

### 1. Obtención de la secuencia proteica

Se utilizó la entrada curada de UniProt:

-   Proteína: MAX_HUMAN\
-   Accession: P61244\
-   Longitud: 160 aa

La secuencia utilizada en la predicción se encuentra en:

data/[Max_sequence_dimer.fasta](data/Max_sequence_dimer.fasta)

El archivo contiene la secuencia sin encabezado FASTA para compatibilidad con AlphaFold3.

------------------------------------------------------------------------

### 2. Construcción del complejo biológico

Se modeló el sistema completo:

| Entidad      | Copias | Descripción                |
|--------------|--------|----------------------------|
| Proteína MAX | 2      | Formación del homodímero   |
| ADN cadena 1 | 1      | Secuencia con motivo E-box |
| ADN cadena 2 | 1      | Cadena complementaria      |

Se diseñó un fragmento de ADN de 25 pb conteniendo el motivo:

CACGTG

Las secuencias utilizadas están en:

data/[Max_Ebox_25bp.fasta](data/MAX_Ebox_25bp.fasta)

El ADN fue definido explícitamente porque AlphaFold3 predice la estructura del ensamblaje proporcionado como entrada.

------------------------------------------------------------------------

### 3. Predicción estructural

Se utilizó:

AlphaFold Server (AlphaFold3)\
<https://alphafoldserver.com>

Configuración:

-   2 copias de MAX
-   2 cadenas complementarias de ADN

El modelo obtenido se encuentra en:

models/[fold_max_dimer_ebox_25bp_af_model_0.cif](models/fold_max_dimer_ebox_25bp_af_model_0.cif)

------------------------------------------------------------------------

### 4. Evaluación de calidad estructural

El modelo fue evaluado con:

SWISS-MODEL Structure Assessment\
<https://swissmodel.expasy.org/assess>

Resultados guardados en:

[results](results/)

------------------------------------------------------------------------

## Interpretación de resultados

El análisis estructural completo y la interpretación biológica se encuentran en:

docs/[REPORT.md](docs/REPORT.md)

------------------------------------------------------------------------
