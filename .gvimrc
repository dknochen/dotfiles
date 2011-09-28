set guioptions-=T

set cursorline
set colorcolumn=80
highlight ColorColumn ctermbg=darkgrey guibg=#1e1e1e

set transparency=2

" colorscheme twilight

set laststatus=2
set showmode
set showcmd
set ruler

set encoding=utf-8

set nowrap
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set smartindent
set list listchars=tab:\ \ ,trail:·

" Tab Completion
set wildignore+=.git,*.pyc,.sass-cache/,.DS_Store,*.mo
set wildmode=list:longest,list:full

" Search
set hlsearch
set incsearch
set ignorecase
set smartcase

" Command-T
" let g:CommandTMaxHeight=20

" au BufRead,BufNewFile {Gemfile,Vagrantfile} set ft=ruby


