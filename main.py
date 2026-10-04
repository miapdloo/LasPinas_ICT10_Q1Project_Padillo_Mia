from pyscript import display, document 
 
def SKU_generator(e): 
    
    document.getElementById('sku_output').innerHTML = "" 
    
   
    category = document.getElementById('category').value.strip() 
    product_name = document.getElementById('name').value.strip() 
    stock_qty = document.getElementById('quantity').value.strip() 

    
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty) 
 
    
    display("Generated SKU: " + sku, target='sku_output') 
