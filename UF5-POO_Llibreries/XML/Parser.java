import javax.xml.parsers.*;
import org.w3c.dom.*;
import java.io.*;
/**
 * Aquesta estructura d'imports sera comu sempre que volguem treballar amb XML en JAVA.
 * Per un costat tenim els Parsers d'XML que seran els encarregats de saber com buscar tota la informacio que 
 * existeix en un XML.
 * Per altra banda tenim W3C DOM, que s'encarrega de crear els objectes amb els que podem treballar i navegar dels
 * arxius de llenguatge de marques, al igual que ho podem fer amb l'inspector de Chrome/Firefox
 */

class Parser
{
    public static void main(String[] args) throws Exception{
        /**
         * El primer que farem sera veure com podem llegir un XML de forma basica
         */
        System.out.println("How to read XML");
        howToReadXML();
        /**
         * Aqui veurem que a banda de navegar tambe podem extreure informacio, com pot ser text
         */
        System.out.println("How to extract data from XML");
        howToExtractDataFromXML();
        /**
         * No nomes podem llegir XML, tambe podem crear fitxers nosaltres des de 0, i aqui veurem com fer-ho
         */
        System.out.println("How to create XML");
        howToCreateAnXML();
    }

    private static void howToReadXML() throws Exception {
        DocumentBuilderFactory builderFactory = DocumentBuilderFactory.newInstance();
        Document document = null;
        
        try {
            DocumentBuilder builder = builderFactory.newDocumentBuilder();
            //Obrim el fitxer, i com que aixo pot portar errors ho fiquem tot dins dun TRY/CATCH
            File f = new File ("elMeuFitxer.xml");
            document = builder.parse(f);
            //Aqui tindriem l'arrel del XML
            Element e = document.getDocumentElement();
            int nreArticles = 0;
            //Aqui estem escollint els fills que siguin de tipus producte mitjancant el TAG
            NodeList l = e.getElementsByTagName("Producte");
            for (int i = 0; i < l.getLength(); i++) {
                Element elem = (Element)l.item(i);
                //Mirem si l'atribut aLaVenda es true o false
                String venda = elem.getAttribute("aLaVenda");
                if ("true".equals(venda)) {
                    nreArticles++;
                }
            }
            System.out.println("Articles a la venda: " + nreArticles);
        } catch (Exception ex) {
            System.out.println("Error en la lectura del document: " + ex);
            //Aqui veiem com tot i que hem capturat l'exepcio la tornem a llencar i que sigui el metode que ens ha invocat
            //qui s'encarregui de gestionar-ho
            throw ex;
        }
    }

    private static void howToExtractDataFromXML() {
        DocumentBuilderFactory builderFactory = DocumentBuilderFactory.newInstance();
        Document document = null;
        
        try {
            DocumentBuilder builder = builderFactory.newDocumentBuilder();
            File f = new File ("elMeuFitxer.xml");
            document = builder.parse(f);
            Element e = document.getDocumentElement();
            //Obtenir tots els nodes del document anomenats "nom"
            NodeList llistaElems = e.getElementsByTagName("Nom");
            //Recorregut d'elements anomenats "Nom"
            for (int i = 0; i < llistaElems.getLength(); i++) {
                Element elem = (Element)llistaElems.item(i);
                NodeList llistaFills = elem.getChildNodes();
                //Recorregut de nodes fill d'un element (text, atributs, etc.)
                String text = "";
                for (int j = 0; j < llistaFills.getLength(); j++) {
                    Node n = llistaFills.item(j);
                    //Mirar si els nodes són de text, com veureu CDATA ho hevist a LMSGI
                    if ( (n.getNodeType() == Node.TEXT_NODE)||
                        (n.getNodeType() == Node.CDATA_SECTION_NODE) ) {
                
                        text += n.getNodeValue();
                    }
                }

                //Arribat aquest punt veureu com aqui podriem extreure el codi per no repetir-nos, queda com a exercici
                NodeList llistaPreus = ((Element)elem.getParentNode()).getElementsByTagName("Preu");
                for (int j = 0; j < llistaPreus.getLength(); j++) {
                    Element preu = (Element)llistaPreus.item(j);
                    NodeList llistaFillsPreu = preu.getChildNodes();
                    for (int k = 0; k < llistaFillsPreu.getLength(); k++) { 
                        Node p = llistaFillsPreu.item(k);
                        //Mirar si els nodes són de text, com veureu CDATA ho hevist a LMSGI
                        if ( (p.getNodeType() == Node.TEXT_NODE)||
                            (p.getNodeType() == Node.CDATA_SECTION_NODE) ) {
                    
                            text += " " + p.getNodeValue();
                        }
                    }
                    System.out.println(text);
                }
            }
        } catch (Exception ex) {
            System.out.println("Error en la lectura del document: " + ex);
        }
    }

    private static void howToCreateAnXML() {
        /**
         * Aqui el que farem sera recrear el que seria el document XML amb el que hem treballat, creant unicament 
         * el primer element. Si ho guardessim en un fitxer veuriem exactament el mateix que hi tenim ja al fitxer,
         * excloent els altres dos productes, pero fent servir els mateixos TAGs que hi han.
         */
        DocumentBuilderFactory builderFactory = DocumentBuilderFactory.newInstance();
        Document document = null;

        try {
            DocumentBuilder builder = builderFactory.newDocumentBuilder();
            document = builder.newDocument();

            // Element arrel
            Element arrel = document.createElement("LlistaProductes");
            document.appendChild(arrel);

            // Element fill de l'arrel
            Element prod = document.createElement("Producte");
            prod.setAttribute("id", "1");
            prod.setAttribute("aLaVenda", "true");

            // Elements fill de l'anterior
            Element fill = document.createElement("Nom");
            fill.setTextContent("Producte 1");
            prod.appendChild(fill);

            fill = document.createElement("Preu");
            fill.setTextContent("10.0");
            prod.appendChild(fill);

            fill = document.createElement("Estoc");
            fill.setTextContent("4");
            prod.appendChild(fill);

            arrel.appendChild(prod);
        } catch (Exception ex) {
            System.out.println("Error en la lectura del document: " + ex);
        }
    }
}