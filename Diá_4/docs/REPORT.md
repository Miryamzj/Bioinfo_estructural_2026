# Interpretación de resultados

## Complejo MAX–DNA (E-box) modelado con AlphaFold3

------------------------------------------------------------------------

## 1. Calidad global del modelo (AlphaFold3)

![AlphaFold results](../resuls/AlphaFold_results.png)

El modelo presenta valores:

-   **ipTM ≈ 0.63**
-   **pTM ≈ 0.62**

Estos valores indican una **interfaz proteína-proteína plausible**, compatible con un dímero estable, aunque no extremadamente rígido.

Esto es consistente con la biología de MAX:

-   MAX dimeriza de forma estable
-   pero la orientación relativa puede variar dependiendo del ADN

El mapa PAE muestra bloques bien definidos para cada monómero y la región del dominio HLH, indicando que la red neuronal reconoce correctamente las unidades estructurales del complejo.

------------------------------------------------------------------------

## 2. Geometría estereoquímica (MolProbity)

![MolProbity metrics](results/swissmodel_molprobity_metrics.png)

Valores principales:

| Métrica | Valor | Interpretación |
|---------------------------|-----------------------|-----------------------|
| MolProbity score | 2.19 | Geometría comparable a estructuras experimentales de resolución media |
| Clashscore | 8.33 | Pocos choques atómicos |
| Rotamer outliers | 1.06% | Muy bajo |
| Bad bonds | 2 / 3750 | Insignificante |
| Bad angles | 29 / 5259 | Bajo |

Esto indica que el modelo es **físicamente plausible** y no contiene errores graves de geometría.

------------------------------------------------------------------------

## 3. Diagrama de Ramachandran

[Ramachandran plot](results/swissmodel_ramachandran.png)

Resultados:

-   81.33% regiones favorecidas
-   Outliers localizados principalmente en extremos

Interpretación:

Los residuos fuera de región corresponden a **colas intrínsecamente desordenadas**, típicas de factores de transcripción bHLH-LZ.\
El dominio estructurado (hélices largas) se encuentra dentro de regiones permitidas.

Por lo tanto, los outliers no representan errores del modelo sino flexibilidad biológica real.

------------------------------------------------------------------------

## 4. Calidad global y local (QMEANDisCo)

![QMEAN](results/swissmodel_qmean_global_local.png)

Valores:

-   **QMEAN Z-score ≈ −3.7**
-   Calidad local alta en el dominio HLH
-   Baja calidad en regiones terminales

Interpretación:

El valor bajo no indica fallo del modelo.\
Los factores que reducen QMEAN son:

-   proteína no globular
-   presencia de ADN
-   regiones desordenadas
-   plegamiento inducido por unión

La zona funcional presenta alta confianza estructural.

------------------------------------------------------------------------

## 5. Cobertura estructural

![Sequence coverage](results/swissmodel_sequence_coverage.png)

Se observa:

-   Núcleo central altamente estructurado
-   Regiones terminales flexibles
-   Dominio bHLH completamente modelado

Esto coincide con el comportamiento experimental de MAX:\
solo se estructura completamente al unirse al ADN.

------------------------------------------------------------------------

## 6. Arquitectura del complejo

![Structure](results/swissmode_structure.png)

El modelo reproduce correctamente:

-   Formación de homodímero
-   Hélices largas tipo leucine zipper
-   Inserción en surco mayor del ADN
-   Reconocimiento del motivo E-box

Las colas permanecen desordenadas, lo cual es biológicamente esperado.

------------------------------------------------------------------------

## Conclusión

El modelo predicho representa un complejo funcionalmente coherente.

La combinación de:

-   confianza estructural local alta
-   geometría correcta
-   interfaz consistente
-   concordancia biológica

indica que la predicción captura adecuadamente la arquitectura real del factor de transcripción MAX unido a ADN.

No es una estructura cristalográfica exacta, pero sí un **modelo mecanísticamente válido del estado funcional del complejo**.
