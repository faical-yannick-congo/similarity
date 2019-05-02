# coding: utf-8
# Standard Python libraries
from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

# http://www.numpy.org/
import numpy as np

# https://github.com/usnistgov/DataModelDict
from DataModelDict import DataModelDict as DM

# https://github.com/usnistgov/atomman
import atomman.unitconvert as uc
from iprPy.tools import aslist

class CalculationRelaxStatic(object):

    def __init__(self, name, content):
        content = DM(content)
        if self.contentroot in content:
            self.__content = content
        else:
            self.__content = self.dicttomodel(content)
        
        self.__name = name

    @property
    def dict(self):
        return self.modeltodict(self.__content)

    @property
    def json(self):
        return self.__content.json()

    @property
    def xml(self):
        return self.__content.xml()

    @property
    def model(self):
        return self.__content

    @property
    def contentroot(self):
        """Schema root element"""
        return 'calculation-relax-static'
    
    def modeltodict(self, model):
        """
        Transforms a tiered data model into a flat dictionary.
        """
        calc = model[self.contentroot]
        params = {}
        params['key'] = calc['key']
        params['script'] = calc['calculation']['script']
        params['atomman_version'] = calc['calculation']['atomman-version']
        params['iprPy_version'] = calc['calculation']['iprPy-version']
        params['LAMMPS_version'] = calc['calculation']['LAMMPS-version']

        params['a_mult1'] = calc['calculation']['run-parameter']['size-multipliers']['a'][0]
        params['a_mult2'] = calc['calculation']['run-parameter']['size-multipliers']['a'][1]
        params['b_mult1'] = calc['calculation']['run-parameter']['size-multipliers']['b'][0]
        params['b_mult2'] = calc['calculation']['run-parameter']['size-multipliers']['b'][1]
        params['c_mult1'] = calc['calculation']['run-parameter']['size-multipliers']['c'][0]
        params['c_mult2'] = calc['calculation']['run-parameter']['size-multipliers']['c'][1]
        params['min_etol'] = calc['calculation']['run-parameter']['energytolerance']
        params['min_ftol'] = uc.value_unit(calc['calculation']['run-parameter']['forcetolerance'])
        params['min_maxiter'] = calc['calculation']['run-parameter']['maxiterations']
        params['min_maxeval'] = calc['calculation']['run-parameter']['maxevaluations']
        params['min_dmax'] = uc.value_unit(calc['calculation']['run-parameter']['maxatommotion'])
        
        params['potential_LAMMPS_key'] = calc['potential-LAMMPS']['key']
        params['potential_LAMMPS_id'] = calc['potential-LAMMPS']['id']
        params['potential_key'] = calc['potential-LAMMPS']['potential']['key']
        params['potential_id'] = calc['potential-LAMMPS']['potential']['id']

        params['load_file'] = calc['system-info']['artifact']['file']
        params['load_style'] = calc['system-info']['artifact']['format']
        params['load_options'] = calc['system-info']['artifact']['load_options']
        params['family'] = calc['system-info']['family']
        params['symbols'] = ' '.join(aslist(calc['system-info']['symbol']))

        params['temperature'] = uc.value_unit(calc['phase-state']['temperature'])
        params['pressure_xx'] = uc.value_unit(calc['phase-state']['pressure-xx'])
        params['pressure_yy'] = uc.value_unit(calc['phase-state']['pressure-yy'])
        params['pressure_zz'] = uc.value_unit(calc['phase-state']['pressure-zz'])
        params['pressure_xy'] = uc.value_unit(calc['phase-state']['pressure-xy'])
        params['pressure_xz'] = uc.value_unit(calc['phase-state']['pressure-xz'])
        params['pressure_yz'] = uc.value_unit(calc['phase-state']['pressure-yz'])

        params['status'] = calc.get('status', 'finished')
        params['error'] = calc.get('error', np.nan)

        if params['status'] == 'finished':
            
            params['initial_load_file'] = calc['initial-system']['artifact']['file']
            params['initial_load_style'] = calc['initial-system']['artifact']['format']
            params['initial_load_options'] = calc['initial-system']['artifact'].get('load_options', None)
            params['initial_symbols'] = ' '.join(aslist(calc['initial-system']['symbols']))
            
            params['final_load_file'] = calc['final-system']['artifact']['file']
            params['final_load_style'] = calc['final-system']['artifact']['format']
            params['final_load_options'] = calc['final-system']['artifact'].get('load_options', None)
            params['final_symbols'] = ' '.join(aslist(calc['final-system']['symbols']))
            
            params['lx'] = uc.value_unit(calc['measured-box-parameter']['lx'])
            params['ly'] = uc.value_unit(calc['measured-box-parameter']['ly'])
            params['lz'] = uc.value_unit(calc['measured-box-parameter']['lz'])
            params['xy'] = uc.value_unit(calc['measured-box-parameter']['xy'])
            params['xz'] = uc.value_unit(calc['measured-box-parameter']['xz'])
            params['yz'] = uc.value_unit(calc['measured-box-parameter']['yz'])

            params['E_cohesive'] = uc.value_unit(calc['cohesive-energy'])
            params['measured_temperature'] = uc.value_unit(calc['measured-phase-state']['temperature'])
            params['measured_pressure_xx'] = uc.value_unit(calc['measured-phase-state']['pressure-xx'])
            params['measured_pressure_yy'] = uc.value_unit(calc['measured-phase-state']['pressure-yy'])
            params['measured_pressure_zz'] = uc.value_unit(calc['measured-phase-state']['pressure-zz'])
            params['measured_pressure_xy'] = uc.value_unit(calc['measured-phase-state']['pressure-xy'])
            params['measured_pressure_xz'] = uc.value_unit(calc['measured-phase-state']['pressure-xz'])
            params['measured_pressure_yz'] = uc.value_unit(calc['measured-phase-state']['pressure-yz'])
        
        else:
            params['initial_load_file'] = np.nan
            params['initial_load_style'] = np.nan
            params['initial_load_options'] = np.nan
            params['initial_symbols'] = np.nan
            
            params['final_load_file'] = np.nan
            params['final_load_style'] = np.nan
            params['final_load_options'] = np.nan
            params['initial_symbols'] = np.nan
            
            params['lx'] = np.nan
            params['ly'] = np.nan
            params['lz'] = np.nan
            params['xy'] = np.nan
            params['xz'] = np.nan
            params['yz'] = np.nan

            params['E_cohesive'] = np.nan
            params['measured_temperature'] = np.nan
            params['measured_pressure_xx'] = np.nan
            params['measured_pressure_yy'] = np.nan
            params['measured_pressure_zz'] = np.nan
            params['measured_pressure_xy'] = np.nan
            params['measured_pressure_xz'] = np.nan
            params['measured_pressure_yz'] = np.nan

        return params
    
    def dicttomodel(self, params, energy_unit='eV', length_unit='angstrom', pressure_unit='GPa'):
        """
        Transforms a flat dictionary into a tiered data model.
        """
        # Create the root of the DataModelDict
        model = DM()
        model[self.contentroot] = calc = DM()

        # Assign uuid
        calc['key'] = params['key']

        # Save calculation parameters
        calc['calculation'] = DM()
        calc['calculation']['iprPy-version'] = params['iprPy_version']
        calc['calculation']['atomman-version'] = params['atomman_version']
        calc['calculation']['LAMMPS-version'] = params['LAMMPS_version']

        calc['calculation']['script'] = params['script']
        calc['calculation']['run-parameter'] = run_params = DM()

        run_params['size-multipliers'] = DM()
        run_params['size-multipliers']['a'] = [params['a_mult1'], params['a_mult2']]
        run_params['size-multipliers']['b'] = [params['b_mult1'], params['b_mult2']]
        run_params['size-multipliers']['c'] = [params['c_mult1'], params['c_mult2']]

        run_params['energytolerance'] = params['min_etol']
        run_params['forcetolerance'] = uc.model(params['min_ftol'], 
                                                energy_unit + '/' + length_unit)
        run_params['maxiterations']  = params['min_maxiter']
        run_params['maxevaluations'] = params['min_maxeval']
        run_params['maxatommotion']  = uc.model(params['min_dmax'],
                                                length_unit)

        # Copy over potential data model info
        calc['potential-LAMMPS'] = DM()
        calc['potential-LAMMPS']['key'] = params['potential_LAMMPS_key']
        calc['potential-LAMMPS']['id'] = params['potential_LAMMPS_id']
        calc['potential-LAMMPS']['potential'] = DM()
        calc['potential-LAMMPS']['potential']['key'] = params['potential_key']
        calc['potential-LAMMPS']['potential']['id'] = params['potential_id']

        # Save info on system file loaded
        calc['system-info'] = DM()
        calc['system-info']['family'] = params['family']
        calc['system-info']['artifact'] = DM()
        calc['system-info']['artifact']['file'] = params['load_file']
        calc['system-info']['artifact']['format'] = params['load_style']
        calc['system-info']['artifact']['load_options'] = params['load_options']
        for symbol in params['symbols'].split(' '):
            calc['system-info'].append('symbol', symbol)

        # Save phase-state info
        calc['phase-state'] = DM()
        calc['phase-state']['temperature'] = uc.model(params['temperature'], 'K')
        calc['phase-state']['pressure-xx'] = uc.model(params['pressure_xx'],
                                                      pressure_unit)
        calc['phase-state']['pressure-yy'] = uc.model(params['pressure_yy'],
                                                      pressure_unit)
        calc['phase-state']['pressure-zz'] = uc.model(params['pressure_zz'],
                                                      pressure_unit)
        calc['phase-state']['pressure-xy'] = uc.model(params['pressure_xy'],
                                                      pressure_unit)
        calc['phase-state']['pressure-xz'] = uc.model(params['pressure_xz'],
                                                      pressure_unit)
        calc['phase-state']['pressure-yz'] = uc.model(params['pressure_yz'],
                                                      pressure_unit)

        if params['status'] != 'finished':
            calc['status'] = params['status']
        else:
            # Save info on initial and final configuration files
            calc['initial-system'] = DM()
            calc['initial-system']['artifact'] = DM()
            calc['initial-system']['artifact']['file'] = params['initial_load_file']
            calc['initial-system']['artifact']['format'] = params['initial_load_style']
            if params['initial_load_options'] is not None:
                calc['initial-system']['artifact']['load_options'] = params['initial_load_options']
            for symbol in params['initial_symbols'].split(' '):
                calc['initial-system'].append('symbols', symbol)

            calc['final-system'] = DM()
            calc['final-system']['artifact'] = DM()
            calc['final-system']['artifact']['file'] = params['final_load_file']
            calc['final-system']['artifact']['format'] = params['final_load_style']
            if params['final_load_options'] is not None:
                calc['final-system']['artifact']['load_options'] = params['final_load_options']
            for symbol in params['final_symbols'].split(' '):
                calc['final-system'].append('symbols', symbol)
            
            # Save measured box parameter info
            calc['measured-box-parameter'] = mbp = DM()
            mbp['lx'] = uc.model(params['lx'], length_unit)
            mbp['ly'] = uc.model(params['ly'], length_unit)
            mbp['lz'] = uc.model(params['lz'], length_unit)
            mbp['xy'] = uc.model(params['xy'], length_unit)
            mbp['xz'] = uc.model(params['xz'], length_unit)
            mbp['yz'] = uc.model(params['yz'], length_unit)

            # Save measured phase-state info
            calc['measured-phase-state'] = mps = DM()
            mps['temperature'] = uc.model(params['measured_temperature'], 'K')
            mps['pressure-xx'] = uc.model(params['measured_pressure_xx'],
                                          pressure_unit)
            mps['pressure-yy'] = uc.model(params['measured_pressure_yy'],
                                          pressure_unit)
            mps['pressure-zz'] = uc.model(params['measured_pressure_zz'],
                                          pressure_unit)
            mps['pressure-xy'] = uc.model(params['measured_pressure_xy'],
                                          pressure_unit)
            mps['pressure-xz'] = uc.model(params['measured_pressure_xz'],
                                          pressure_unit)
            mps['pressure-yz'] = uc.model(params['measured_pressure_yz'],
                                          pressure_unit)
            
            # Save the final cohesive energy
            calc['cohesive-energy'] = uc.model(params['E_cohesive'], energy_unit)

        return model