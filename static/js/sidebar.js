// $(document).ready(function(){
//     toggleSidebar();
// });
//
//
// // function to show or hide sidebar when categories is clicked
// function toggleSidebar() {
//     let sidebarHolder = $('#sidebarHolder')[0];
//     if(sidebarHolder.style.left === '-250px'){
//         sidebarHolder.style.left = '0';
//     } else {
//         sidebarHolder.style.left = '-250px';
//     }
// }
//
//
// function showSubcategories(_this) {
//     try{
//         _this.classList.add('active-li');
//         let subcategorLis = $(`#subcategories li`);
//         let dNoneDiv = subcategorLis[0].parentElement.parentElement.parentElement.parentElement;
//         dNoneDiv.classList.remove('d-none');
//         subcategorLis.each(function (index, item) {
//             if(item.getAttribute('data-id') === _this.id ){
//                  item.classList.remove('d-none');
//             }
//         });
//     } catch(err){
//         console.log(err);
//     }
// }
//
//
// function hideSubcategories(_this) {
//     try{
//         _this.classList.remove('active-li');
//         let subcategorLis = $(`#subcategories li`);
//         let dNoneDiv = subcategorLis[0].parentElement.parentElement.parentElement.parentElement;
//         dNoneDiv.classList.add('d-none');
//         subcategorLis.each(function (index, item) {
//             if(item.getAttribute('data-id') === _this.id){
//                  item.classList.add('d-none');
//             }
//         });
//     }catch(err){
//         console.log(err);
//     }
// }
//
//
// function showMoreCategories(_this){
//     try{
//         _this.classList.remove('active-li');
//         let subcategorLis = $(`#moreCategories li`);
//         let dNoneDiv = subcategorLis[0].parentElement.parentElement.parentElement.parentElement;
//         dNoneDiv.classList.add('d-none');
//         subcategorLis.each(function (index, item) {
//             if(item.getAttribute('data-id') === _this.id){
//                  item.classList.add('d-none');
//             }
//         });
//     }catch(err){
//         console.log(err);
//     }
// }
//
//
// function hideMoreCategories(){
//     try{
//         let subcategorLis = $(`#subcategories #${_this.id}`);
//         let dNoneDiv = subcategorLis[0].parentElement.parentElement.parentElement.parentElement;
//         dNoneDiv.classList.add('d-none');
//         subcategorLis.each(function (index, item) {
//             item.classList.add('d-none');
//         });
//     }catch(err){
//         console.log(err);
//     }
// }
//
//
// // function to add light grey background to more categories item when mouse enters it
// function addGreyBackground(_this) {
//     _this.style.backgroundColor = '#e9ecef';
// }
//
//
// // function to remove light grey background to more categories item when mouse leaves it
// function removeGreyBackground(_this) {
//     _this.style.backgroundColor = '';
// }
