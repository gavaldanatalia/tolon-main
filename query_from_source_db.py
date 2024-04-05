# Import library

def query_supplier():
    """
    ¿Qué devuelve esta query:
        --Todas las personas físicas / autonomos que deben aparecer en el selector
        --Aquellas personas físicas o autónomos que se le ha facturado >=2000 en los últimos tres años
        --Aquellas personas físicas o autónomos que se les haya facturado algo por primera vez en el año en curso
    """

    sql = """
    select distinct 
        or_supplier.sup_id as sup_id, 
        or_supplier.sup_corporatename as sup_corporatename,
        current_timestamp as fecha_registro
        from "DOCHEADER_DOH" or_docheader_compra 
        inner join "SUPPLIER_SUP" or_supplier on or_supplier.sup_id = sup_doh_fk
        where tas_sup_fk <> 22 and age_sup_fk is not null 
        
        union 
        
        select sup_id, sup_corporatename, current_timestamp as fecha_registro
        from (
        select 
        or_supplier.sup_id as sup_id, 
        or_supplier.sup_corporatename as sup_corporatename,
        sum(doh_amount)
        from "DOCHEADER_DOH" or_docheader_compra 
        inner join "SUPPLIER_SUP" or_supplier on or_supplier.sup_id = sup_doh_fk
        where tas_sup_fk = 22 and age_sup_fk is not null 
        group by or_supplier.sup_id, or_supplier.sup_corporatename 
        having sum(doh_amount) >= 500 or extract(year from min(or_docheader_compra.doh_date)) = extract(year from CURRENT_DATE)) 
    """

    return sql

def query_articulos():
    """
        ¿Qué devuelve esta query?:
        Productos que recogen los chóferes de los camiones
    """
    sql = """
    
        select distinct
        or_item.ite_id  as ite_id, 
        or_item.ite_name  as ite_name
        from "DOCHEADER_DOH" or_docheader_compra 
        inner join "DOCLINE_DLI" or_docline_compra on or_docline_compra.doh_dli_fk = or_docheader_compra.doh_id
        inner join "ITEM_ITE" or_item  on or_item.ite_id  = or_docline_compra.ite_dli_fk
        where LENGTH(or_item.ite_id)<=8 

        """

    return sql

def query_categoria_producto():
    """
        ¿Qué devuelve esta query?:
        Las categorias de los productos, las familias de los productos
    """

    sql = """
    select itc_id, itc_description, current_timestamp as fecha_registro 
    from "ITEMCATEGORY_ITC" ii 
    """

    return sql


def query_header_compras():
    """
        ¿Qué devuelve esta query?:
        Las cabeceras de los albaranes de compra
    """

    sql = """
    select 
        dd.doh_id as doh_id, 
        dd.doh_date as doh_date,
        dd.sup_doh_fk as sup_doh_fk, 
        dd.war_doh_fk as war_doh_fk, 
        dd.doh_amount as doh_amount, 
        dd.doh_netamount as doh_netamount, 
        upper(dd.doh_n_matricula) as doh_n_matricula, 
        dd.doh_type as doh_type, 
        'ALBARANES DE COMPRA' as doc_type,
        current_timestamp as fecha_registro
        from "DOCHEADER_DOH" dd 
        where dd.doh_type = 12  
        and extract(year from dd.doh_date) >= extract(year from CURRENT_DATE)
    """
    return sql

def query_lines_compras():
    """
        ¿Qué devuelve esta query?:
        Las líneas de los albaranes de compra
    """
    sql = """
    select
    dli.doh_dli_fk, 
    dli.dli_quantity, 
    dli.dli_price, 
    dli.dli_totalamount,
    dli.ite_dli_fk,
    current_timestamp as fecha_registro
    from "DOCLINE_DLI" dli
    inner join "DOCHEADER_DOH" dd on  dd.doh_id = dli.doh_dli_fk
    where dd.doh_type = 12  
    and extract(year from dd.doh_date) >= extract(year from CURRENT_DATE)-3
    """
    return sql

def query_agentes_proveedores():
    """
        ¿Qué devuelve esta query?:
        Las comerciales de cada uno de los proveedores
    """
    sql = """
        select age_id, age_order, age_name, current_timestamp as fecha_registro from "AGENT_AGE" aa 
        """
    return sql
